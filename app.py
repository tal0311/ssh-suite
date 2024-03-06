import eel
import state
from  services_py.ssh_service import SSHConnection
import json 
import time
from services_py.http_service import HTTPService
import services_py.svg_service as svg_service

ssh_connection = None

eel.init('web')
app_state = state.AppState()
user_http = HTTPService('/api/user')
size = app_state.get_state('size')

@eel.expose
def toggle_terminal():
    print('toggle_terminal')

@eel.expose
def initial_commands():
    pass

@eel.expose
def get_icon(icon_name):
    return svg_service.get_svg(icon_name)

@eel.expose
def get_folder_details(folder_name):
   global ssh_connection
   ssh_connection.execute_command('cd' ,folder_name)
   output= ssh_connection.execute_command('ls -lh' ,folder_name)
   curr_dir= ssh_connection.current_directory
   print(output, curr_dir)
   eel.js_render_folder_details(output, curr_dir)
    
@eel.expose
def get_file_details(file_name):
    print('file_name:', file_name)
    global ssh_connection
    output= ssh_connection.execute_command('cat' ,file_name)
    print('cat :', output)
    eel.js_render_file_details(output)
    
@eel.expose
def get_back():
    global ssh_connection
    ssh_connection.execute_command('cd' ,'-')
    output= ssh_connection.execute_command('ls -lh', '.')
    eel.js_render_folder_details(output)

@eel.expose
def send_mail():
    print('send_mail')
    # send mail with shell command
    
    
@eel.expose
def upload_file():
    print('upload_file')
    # upload file with scp command
    # To upload a file using scp command, you can use the following command:
    # scp /path/to/local/file username@hostname:/path/to/remote/directory
    # Please replace the paths, username, and hostname with your actual data.
    
    
@eel.expose
def init_app():
   
    global ssh_connection
    try:
        connection_info = app_state.get_state('ssh_connection') 
        ssh_connection = SSHConnection(connection_info['hostname'], connection_info['port'], connection_info['username'], connection_info['password'])
        ssh_connection.connect()
       
        ssh_connection.execute_command('whoami')
        print('Initial commands\n')
        output= ssh_connection.execute_command('ls -lh')
        eel.js_render_folder_details(output)
       
              
    except Exception as e:
        print("An error occurred:", e)
        return {'status': 'error', 'message': str(e)}
    
@eel.expose
def get_breadcrumbs(dir):
    return app_state.get_state('current_folder')
    
try:
    eel.start('index.html', size=(size['width'], size['height']), port=0)
except (SystemExit, MemoryError, KeyboardInterrupt):
    print("Program Exit, Save Logs if Needed")
