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
        print('command:', command , 'target:', target)
        if self.client:
    # Directly execute 'cd' commands and update current directory
            if command == 'cd':
                # Get the directory part of the command
                self.change_directory(target)  # Attempt to change directory
                return self.current_directory
            else:
            # For all other commands, execute them in the context of the current directory
                if target and command != 'cat':
                 full_command = f'{command} {target}'
                else:
                 full_command = command
                 
                stdin, stdout, stderr = self.client.exec_command(full_command)
                

            # Special handling for 'cat' to return the content as a single string
                if command == 'cat':
                    full_command = f'cat {self.current_directory}/{target}'
                    print('full_command:', full_command) 
                    stdin, stdout, stderr = self.client.exec_command(full_command)
                    return stdout.read().decode('utf-8').strip()

            # Default handling for other commands
                return stdout.read().decode('utf-8').split('\n')[:-1]


    def update_current_directory(self):
        # Execute 'pwd' to get the current working directory on the remote server
        stdin, stdout, stderr = self.client.exec_command('pwd')
        self.current_directory = stdout.read().strip().decode('utf-8')

    def change_directory(self, directory):
        # Try to change directory and update the current directory
        test_command = f'cd {directory}; pwd'
        stdin, stdout, stderr = self.client.exec_command(test_command)
        output = stdout.read().strip().decode('utf-8')
        if output:  # Successfully changed directory
            self.current_directory = output
        else:
            print("Failed to change directory.")

    def transfer_file_scp(self, local_path, remote_path):
        if self.client:
            # Create an SCPClient object using the existing SSH connection
            with SCPClient(self.client.get_transport()) as scp:
                # Copy the file from the local path to the remote path
                scp.put(local_path, remote_path)

# Example usage remains the same
