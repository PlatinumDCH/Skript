from pathlib import Path
from errors.specific import NotExists, NotIsDirectory
class DirectoryPathDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        """get current value atr"""
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        directory_path = Path(value)
        if not directory_path.exists():
            raise NotExists(f"The specified path does not exist: {value}")

        if not directory_path.is_dir():
            raise NotIsDirectory(f"The specified path is not a directory: {value}")

        isinstance.__dict__[self.name] = directory_path

    def __delete__(self, instance):
        del instance.__dict__[self.name]

