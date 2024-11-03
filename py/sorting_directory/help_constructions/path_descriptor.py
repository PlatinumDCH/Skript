from pathlib import Path
from py.sorting_directory.errors.specific import NotIsDirectory, NotExists
class DirectoryPathDescriptor:
    def __init__(self, path):
        self.path = Path(path)
        self.validate_directory()

    def __get__(self, instance, owner):
        """get current value atr"""
        return self.path

    def __set__(self, instance, value):
        self.path  = Path(value)
        self.validate_directory()

    def validate_directory(self):

        if not self.path.exists() or not self.path.is_dir():
            raise ValueError(f"The path '{self.path}' is not a valid directory.")

