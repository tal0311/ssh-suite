import paramiko
from scp import SCPClient


class SSHConnection:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.client = None
        # Initialize the current directory as None
        self.current_directory = None

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.hostname, self.port, self.username, self.password)
        # Initialize the current directory upon connection
        self.update_current_directory()

    def disconnect(self):
        if self.client:
            self.client.close()

    def execute_command(self, command, target = None):
        if self.client:
            if command == 'cd':
                self.change_directory(target) 
                return self.current_directory
            else:
                if target and command != 'cat':
                 full_command = f'{command} {target}'
                else:
                 full_command = command
                 
                stdin, stdout, stderr = self.client.exec_command(full_command)
                

                if command == 'cat':
                    full_command = f'cat {self.current_directory}/{target}'
                    print('full_command:', full_command) 
                    stdin, stdout, stderr = self.client.exec_command(full_command)
                    return stdout.read().decode('utf-8').strip()

                return stdout.read().decode('utf-8').split('\n')[:-1]


    def update_current_directory(self):
        stdin, stdout, stderr = self.client.exec_command('pwd')
        self.current_directory = stdout.read().strip().decode('utf-8')

    def change_directory(self, directory):
        test_command = f'cd {directory}; pwd'
        stdin, stdout, stderr = self.client.exec_command(test_command)
        output = stdout.read().strip().decode('utf-8')
        if output: 
            self.current_directory = output
        else:
            print("Failed to change directory.")

    def transfer_file_scp(self, local_path):
        if self.client:
            try:
                
                with SCPClient(self.client.get_transport()) as scp:
                 
                    scp.put(local_path, self.current_directory)
                    print("File transferred successfully!")
            except (paramiko.ssh_exception.SSHException, FileNotFoundError) as e:
                print(f"Error occurred: {e}")


    def download_file_scp(self, local_path):
        if self.client:
            
            remote_path= self.current_directory+'/'+local_path
            with SCPClient(self.client.get_transport()) as scp:
                scp.get(remote_path)

