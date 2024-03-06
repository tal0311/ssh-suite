class AppState:
    def __init__(self):
        self._state = {
            "active_connection": None,
            "filterBy": {},
            "sortBy": {},
            "current_folder": "/home/tal0311",
            "whoami": "tal0311",
            "logged_user": {"username": "tal", "password": "123456"},
            "ssh_connection": {
                "hostname": "192.168.93.98",
                "port": 22,
                "username": "tal0311",
                "password": "123456"
                           },
            "size":{
                "width": 500,
                "height": 500
                 }
            }

    def update_state(self, key, value):
        if key:
          self._state[key] = value
   

    def get_state(self, key):
        if not key: return self._state
        return self._state[key]
    
    