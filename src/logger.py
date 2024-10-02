import logging 
import os
from datetime import datetime

# Define log file with current timestamp
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path to the 'logs' directory
logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)


# Full path to the log file
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)