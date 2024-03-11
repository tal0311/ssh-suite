import os
import datetime


class NotificationManager:
    def __init__(self, file_path='user_actions.log'):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                file.write("User Actions Log\n")
                file.write("-----------------\n")

    def log_action(self, user_name, action):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - User {user_name}: {action}\n"
        with open(self.file_path, 'a') as file:
            file.write(log_entry)
        print("Action logged successfully.")

    def display_logs(self):
        try:
            with open(self.file_path, 'r') as file:
                print("User actions log:")
                # print(file.read())
                return file.read()
        except FileNotFoundError:
            print("Log file not found.")


