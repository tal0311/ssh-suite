import eel
import state
from  services_py.ssh_service import SSHConnection
import json 
import time

ssh_connection = None

eel.init('web')
app_state = state.AppState()
size = app_state.get_state('size')

@eel.expose
def initial_commands():
    pass

@eel.expose
def get_folder_details(folder_name):
   global ssh_connection
   ssh_connection.execute_command('cd' ,folder_name)
   output= ssh_connection.execute_command('ls -lh' ,folder_name)
   print(output)
   eel.js_render_folder_details(output)
    
@eel.expose
def get_file_details(file_name):
    print('file_name:', file_name)
    global ssh_connection
    output= ssh_connection.execute_command('cat' ,file_name)
    print('cat :', output)
    eel.js_render_file_details(output)
    
    

@eel.expose
def init_app():
   
    global ssh_connection
    try:
        connection_info = app_state.get_state('ssh_connection') 
        ssh_connection = SSHConnection(connection_info['hostname'], connection_info['port'], connection_info['username'], connection_info['password'])
        ssh_connection.connect()
       
        ssh_connection.execute_command('whoami')
        print('---------------------')
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
