import eel
import state
from  services_py.ssh_service import SSHConnection
import json 
import time
from services_py.http_service import HTTPService
import services_py.svg_service as svg_service
import services_py.error_service as error_service
import services_py.notification_service as notification_service
import services_py.modal_service as modal_service
import subprocess

# TODO: Add breadcrumbs to the app
# TODO: Add a notification
# TODO: connect to BE
ssh_connection = None

eel.init('web')
app_state = state.AppState()
modal= modal_service.ModalService()
auth_http = HTTPService('/api/auth')
err_service= error_service.ErrorService()
note_service= notification_service.NotificationManager()
size = app_state.get_state('size')

def log(message):
    user= app_state.get_state('whoami')
    note_service.log_action(user, message)
    logs= note_service.display_logs()
    logs= logs.split('\n')
    logs_for_display= logs[len(logs)-10:-1]
    eel.js_render_logs(logs_for_display)

@eel.expose
def toggle_terminal():
    try:
        
        subprocess.run(['start', 'powershell'], shell=True)
        log('Terminal Opened')
        
      
    except Exception as e:
        
        err_service.log_error('Error | '+ str(e) + ' | At: toggle_terminal')
@eel.expose
def initial_commands():
    pass

@eel.expose
def get_icon(icon_name):
    return svg_service.get_svg(icon_name)

@eel.expose
def get_folder_details(folder_name):
    try:
        global ssh_connection
        ssh_connection.execute_command('cd' ,folder_name)
        output= ssh_connection.execute_command('ls -lh' ,folder_name)
        curr_dir= ssh_connection.current_directory
        log('Folder details for: '+ folder_name)
        eel.js_render_folder_details(output, curr_dir)
    except Exception as e:
        
        err_service.log_error('Error | '+ str(e) + ' | At: get_folder_details') 
        
@eel.expose
def get_file_details(file_name):
    try:
        # global ssh_connection
        output= ssh_connection.execute_command('cat' ,file_name)
        log('File details for: '+ file_name)
        eel.js_render_file_details(output)
    except Exception as e:
        
        err_service.log_error('Error | '+ str(e) + ' | At: get_file_details')
    
@eel.expose
def get_back():
    global ssh_connection
    ssh_connection.execute_command('cd' ,'-')
    output= ssh_connection.execute_command('ls -lh', '.')
    eel.js_render_folder_details(output)

@eel.expose
def send_mail():
    print('send_mail')
    log('Mail Sent')
    
    
@eel.expose
def upload_file(local_path):
    try:
       ssh_connection.transfer_file_scp(local_path)
       log('File uploaded')
    except Exception as e:
        
        err_service.log_error('Error | '+ str(e) + ' | At: upload_file')
        
@eel.expose
def download_file(username):
    
    log('File downloaded')
    ssh_connection.download_file_scp(username)

@eel.expose
def get_modal(modal_type):
    try:
        modal_desc= modal.get_modal(modal_type)
        log('Modal opened: '+ modal_type)
        return modal_desc
    except Exception as e:
        err_service.log_error('Error | '+ str(e) + ' | At: get_modal')
        
@eel.expose
def set_conn(conn_info):
    print(conn_info)
    try:    
        info= {"hostname": conn_info['hostname'], "port": conn_info['port'], "username": conn_info['username'], "password": conn_info['password']}
        app_state.update_state('ssh_connection', info)
        app_state.get_state('ssh_connection')
        log('Connection set: ' + str(conn_info))
        
    except Exception as e:
        err_service.log_error('Error | '+ str(e) + ' | At: set_conn')
    
@eel.expose
def signin(credentials):
    try:
        print('signing in')
        # auth_http.post('signin',credentials)
        # app_state.update_state('whoami', user)
        log('User signed in: '+ credentials)
        # return user
    except Exception as e:
        err_service.log_error('Error | '+ str(e) + ' | At: signin')
        return 'Error'
    
    
@eel.expose
def init_app():
   
    global ssh_connection
    try:
        connection_info = app_state.get_state('ssh_connection') 
        ssh_connection = SSHConnection(connection_info['hostname'], connection_info['port'], connection_info['username'], connection_info['password'])
        ssh_connection.connect()
       
        logged_user= ssh_connection.execute_command('whoami')
        output= ssh_connection.execute_command('ls -lh')
        log('App initialized')
        eel.js_render_folder_details(output)
        return logged_user
       
              
    except Exception as e:
        err_service.log_error('Error | '+ str(e) + ' | at init_app')
        return 'Error'
      
    
@eel.expose
def get_breadcrumbs(dir):
    return app_state.get_state('current_folder')
    
try:
    eel.start('index.html', size=(size['width'], size['height']), port=0)
except (SystemExit, MemoryError, KeyboardInterrupt):
    print("Program Exit, Save Logs if Needed")


