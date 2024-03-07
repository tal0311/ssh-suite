class ErrorService:
    def __init__(self, filename='err_logs.log'):
        self.errors = []
        self.filename = filename
        # Create the file if it doesn't exist
        with open(self.filename, 'a'):
            pass

    def log_error(self, error_message):
        """
        Log an error message to file, print it in red, and return it.
        """
        # ANSI escape code for red color
        RED = '\033[91m'
        RESET = '\033[0m'

        with open(self.filename, 'a') as file:
            file.write(error_message + '\n')
        print(RED + error_message + RESET)  # Print error message in red
        self.errors.append(error_message)
        return error_message

    def read_log(self):
        """
        Read and present the contents of the log file.
        """
        with open(self.filename, 'r') as file:
            print("Log File Content:")
            for line in file:
                print(line.rstrip())  # rstrip to remove newline characters

    def get_errors(self):
        """
        Get all logged errors.
        """
        return self.errors

    def clear_errors(self):
        """
        Clear all logged errors.
        """
        self.errors = []

# Example usage:
error_service = ErrorService()

