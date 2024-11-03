import logging
from pathlib import Path
from abc import ABC, abstractmethod

from create_dir import create_dir
from moved_file import move_file
from my_logger import setup_logger
from config import PathConfig
from help_constructions.path_descriptor import DirectoryPathDescriptor

logger = setup_logger(__name__, level=logging.DEBUG, log_file=None)

class AbstractFileManager(ABC):

    @abstractmethod
    def sort_files_by_extension(self):
        ...

    @abstractmethod
    def create_target_directory(self, target_dir: Path):
        ...

    @abstractmethod
    def move_file(self, file: Path, target_dir: Path):
        ...
class FileManager(AbstractFileManager):
    """main class"""
    directory = DirectoryPathDescriptor(PathConfig.main_path.value)

    def __init__(self,directory):
        """use descriptor checking"""
        self.directory = directory

    def sort_files_by_extension(self):
        files = self.get_files()
        for file in files:
            self.process_file(file)

    def get_files(self):
        directory = self.directory
        return [file for file in directory.iterdir() if file.is_file()]

    def process_file(self, file: Path):
        file_extension = file.suffix[1:]
        if not file_extension:
            return
        target_dir = self.directory / file_extension
        self.create_target_directory(target_dir)
        self.move_file(file, target_dir)


    def create_target_directory(self,target_dir: Path):
        create_dir(target_dir)
        logger.info(f"Created directory: {target_dir}")


    def move_file(self,file: Path, target_dir: Path):
        move_file(file, target_dir)
        logger.info(f"Move {file.name} -> {target_dir}")

def main(input_dir: str):
    file_manager = FileManager(input_dir)
    file_manager.sort_files_by_extension()

if __name__ == '__main__':

    path = Path(PathConfig.main_path.value)
    main(path)

