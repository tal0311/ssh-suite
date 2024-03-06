# import paramiko
# import time

# class SSHConnection:
#     def __init__(self, hostname, port, username, password):
#         self.hostname = hostname
#         self.port = port
#         self.username = username
#         self.password = password
#         self.ssh_client = paramiko.SSHClient()
#         self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         self.curr_sell = None

#     def connect(self):
#         try:
#             self.ssh_client.connect(self.hostname, self.port, self.username, self.password)
#             self.curr_sell= self.ssh_client.invoke_shell()
#             print("Connected to remote SSH server")
#         except paramiko.AuthenticationException:
#             print("Authentication failed. Please check your credentials.")
#         except paramiko.SSHException as e:
#             print(f"SSH connection failed: {e}")

#     def execute_command(self, command):
#         print(f"Executing command: {command}")
#         stdin, stdout, stderr = self.curr_sell.exec_command(command)
#         output = stdout.read().decode('utf-8')
#         error = stderr.read().decode('utf-8')
#         return_as_list = ['ls -lh', 'pwd', 'uname -a', 'whoami', 'cat']
        
#         if error:
#             print(error)
            
#         if output:
#             print(output)
#             if 'ls -lh' in command  :
#                 res =output.strip().split('\n')
#                 print(res)
#                 return res
            
#             if  'pwd' in command:
#                 res =output.strip()
#                 print( 'pwd',res)
#                 return res
        
#             if 'uname -a' in command:
#                 res =output.strip()
#                 print(res)
#                 return res
            
#             if 'whoami' in command:
#                 res =output.strip()
#                 print(res)
#                 return res  
            
#             if 'cat' in command:
#                 return output
            
#             if 'cd' in command:
#                 print('cd command')
            
            
            
       

#     def close(self):
#         self.ssh_client.close()
#         print("SSH connection closed.")

# # SSH connection details
# # hostname = '192.168.93.98'
# # port = 22  # Default SSH port
# # username = 'tal0311'
# # password = '123456'

# # # Create SSHConnection object
# # ssh_connection = SSHConnection(hostname, port, username, password)

# # # Connect to remote SSH server
# # ssh_connection.connect()

# # # Execute command on the remote server
# # commands = ['ls', 'pwd', 'uname -a', 'whoami']
# # for command in commands:
# #     time.sleep(1)
# #     ssh_connection.execute_command(command)



# # # Close SSH connection
# # ssh_connection.close()
import paramiko
import time
import re

class SSHConnection:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.curr_shell = None

    def connect(self):
        try:
            self.ssh_client.connect(self.hostname, self.port, self.username, self.password)
            self.curr_shell = self.ssh_client.invoke_shell()
            print("Connected to remote SSH server")
        except paramiko.AuthenticationException:
            print("Authentication failed. Please check your credentials.")
        except paramiko.SSHException as e:
            print(f"SSH connection failed: {e}")

    def execute_command(self, command):
        print(f"Executing command: {command}")
        self.curr_shell.send(command + '\n')
        time.sleep(0.5)  # Optional: add a delay before reading output
        # output = self.curr_shell.recv(4096).decode('utf-8')
        output = self.curr_shell.recv(4096).decode('utf-8')
        print('output:', output)
        
        if 'ls -lh' in command  :
            
            output= re.sub(r'\x1b\[[0-9;]*m', '', output)
            output = output.replace('\r', '\n')
            print('cleaned_output:',output)
            return output
        
        if 'pwd' in command:
            
            return output.strip()
        
      
        
            # print('cleaned_output:', cleaned_output)
    
    
    # Define the function to clean the provided output
    def clean_terminal_output(self,raw_output):
        # Import the re module for regular expression operations
        

        # Remove ANSI escape sequences
        cleaned_output = re.sub(r'\x1b\[[0-9;]*m', '', raw_output)

        # Replace carriage returns with newlines
        cleaned_output = cleaned_output.replace('\r', '\n')

        # Optionally, you can further clean up by removing lines that are not necessary
        # For this example, we'll keep it simple and focus on removing ANSI codes and replacing \r with \n
        
        return cleaned_output.split('\n')


    

    def close(self):
        self.ssh_client.close()
        print("SSH connection closed.")


