import logging
import os
from datetime import datetime

## creating variable that will hold the log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

## logs folder path
logs_path = os.path.join(os.getcwd(), "logs") ## logs : folder name
os.makedirs(logs_path, exist_ok=True) ## if logs folder does not exist then it will be created
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE) ## joining file with the logs folder path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)