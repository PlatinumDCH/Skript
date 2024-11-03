import os
import shutil
from pathlib import Path
from my_logger import setup_logger
import logging

logger = setup_logger(__name__, level=logging.DEBUG, log_file=None)

def is_correct_path(input_path:str)->bool:
    path = Path(input_path)
    return path.is_dir() and path.exists()

def convert_path_str(path:str)-> Path:
    return Path(path)

def move_file(file_path:Path,target_dir:Path)->None:
    shutil.move(str(file_path), target_dir / file_path.name)

def sort_files_by_extension(input_dir:str):

    if not is_correct_path(input_dir):
        logger.error(f'Could not find directory: {input_dir}')
        return

    directory = convert_path_str(input_dir)

    for file_path in directory.glob('*'):
        if file_path.is_file():
            file_extension = file_path.suffix[1:]
            if not file_extension:
                file_extension = 'no_extension'

            target_dir = directory / file_extension
            target_dir.mkdir(exist_ok=True)

            move_file(file_path,target_dir)
            logger.info(f"Move {file_path} -> {target_dir / file_path.name}")



if __name__ == '__main__':

    path = Path()
    sort_files_by_extension(path)