import os
from datetime import datetime, timedelta
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s - %(message)s'
)

loger = logging.getLogger(__name__)

def clear_old_file(directory, days=50):
    cutoff_date = datetime.now() - timedelta(days=days)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_modified_time < cutoff_date:
                os.remove(file_path)
                logging.info(f'file {filename} is delete')
            else:
                logging.info(f"file {filename} not deleted, it's updated later {cutoff_date}")



