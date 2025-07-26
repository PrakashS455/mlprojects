import logging
import os
from datetime import datetime

# Step 1: Define folder and log file name
log_folder = os.path.join(os.getcwd(), "logs")
os.makedirs(log_folder, exist_ok=True)

log_filename = f"{datetime.now().strftime('%Y-%m-%d')}.log"
log_file_path = os.path.join(log_folder, log_filename)

# Step 2: Setup logging
logging.basicConfig(
    filename=log_file_path,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

