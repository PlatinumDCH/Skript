from main import create_dir
from moved_file import move_file
from pathlib import Path
from file_help import FileHelper
from my_logger import setup_logger
import logging
from config import PathConfig
logger = setup_logger(__name__, level=logging.DEBUG, log_file=None)


def main(input_dir:str):
    input_path = FileHelper(input_dir)

    if not input_path.is_valid_file():
        logger.error(f'Could not find directory: {input_dir}')
        return

    directory = input_path.file_path

    files = [file for file in directory.iterdir() if file.is_file()]
    for file in files:
        file_extension = file.suffix[1:]
        if not file_extension:
            continue
        target_dir = directory / file_extension
        create_dir(target_dir)
        move_file(file, target_dir)
        logger.info(f"Move {file.name} -> {target_dir}")



if __name__ == '__main__':

    path = Path(PathConfig.main_path.value)
    main(path)