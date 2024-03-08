class ModalService:
       
    def get_modal(self, modal_type):
        
        if modal_type == "login":
            return self.login_modal()
        if modal_type == "connect":
            return self.connect_modal()
        if modal_type == "ftp":
            return self.ftp_modal()

   
    
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
            "title": "FTP",
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
            "buttons": [
                {"label": "Signin", "function": "signin"},
             
            ]
        }