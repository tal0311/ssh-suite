class ModalService:
       
    def get_modal(self, modal_type):
        print('modal_type service:', modal_type)
        if modal_type == "login":
            return self.login_modal()
        if modal_type == "connect":
            return self.connect_modal()
        if modal_type == "ftp":
            return self.ftp_modal()
        if modal_type== 'ftp_get':
            return self.ftp_get()
        if modal_type== 'sign_in':
            return self.signIn_modal()

   
    
    def login_modal(self):
        return {
            "title": "Login",
            "content": "Please enter your credentials",
            "fields": [
                {"label": "Username", "type": "text", "name": "username"},
                {"label": "Password", "type": "password", "name": "password"}
            ],
            "button": {"label": "Login", "function": "login"},
             
            
        }
    
    def connect_modal(self):
         return {
            "title": "Connect",
            "content": "Please enter your connection details",
            "fields": [
                {"label": "Hostname", "type": "text", "name": "hostname"},
                {"label": "Port", "type": "number", "name": "port"},
                {"label": "Username", "type": "text", "name": "username"},
                {"label": "Password", "type": "password", "name": "password"}
            ],
           
            "button":{ "label":"Connect", "function": "connect"},
             
            
        }
    
    def ftp_modal(self):
        return {
            "title": "Upload File FTP",
            "content": "Please enter your FTP details",
            "fields": [
              
               
                {"label": "Past file full path location", "type": "text", "name": "path"}
            ],
            
            "button": {"label": "Send file", "function": "onUploadFile"},
             
            
        }
        
    def signIn_modal(self):
        return {
            "title": "Sign in",
            "content": "Please enter your credentials",
            "fields": [
                {"label": "Username", "type": "text", "name": "username"},
                {"label": "Password", "type": "password", "name": "password"}
            ],
            "button": {"label": "Signin", "function": "signin"},
             
            
        }
        
    def ftp_get(self):
        return {
            "title": "Get File FTP",
            "content": "Please enter your FTP details",
            "fields": [
                {"label": "Local user name", "type": "text", "name": "username"},
                
            ],
            "button" : {"label": "Download", "function": "onDownloadFile"},
                
            
        }