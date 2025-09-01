import sys


class USvisaException(Exception):
    def __init__(self, error_message):
        self.error_message = error_message
        _, _, exc_tb = sys.exc_info()  # get traceback directly here
        if exc_tb:  # check if traceback exists get the file name and error line
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.file_name = None

    def __str__(self):
        if self.lineno and self.file_name:
            return f"Error occurred in python script name [{self.file_name}] line number [{self.lineno}] error message [{str(self.error_message)}]"
        else:
            return f"Error message: {str(self.error_message)}"
