import sys
import os
from src.logger import logging


# Function to provide detailed error information
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Formatting the error message with file name, line number, and error details
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message

# Custom exception class
class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys):
        # Pass the base exception message
        super().__init__(error_message)
        # Create a detailed error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        # Log the error message for debugging purposes
        logging.error(self.error_message)
        
    def __str__(self):
        return self.error_message  
    
# Main block (entry point)
if __name__=="__main__": ## entry point of code or project
    logging.info("Logging has started")

    try:
        # Code that causes an exception (division by zero)
        a=1/0
    except Exception as e:
        # Log the error and raise the custom exception with the original exception details
        logging.info('Division by zero') 
        raise CustomException(e,sys)