from pathlib import Path

class FileHelper:
    def __init__(self, file_path):
        self.file_path = self._convert_to_path(file_path)

    @staticmethod
    def _convert_to_path(path):
        """str->Path obj"""
        return Path(path)

    def is_valid_file(self):
        return self.is_dr() and self.is_exists()

    def is_fl(self):
        return self.file_path.is_file()

    def is_dr(self):
        return self.file_path.is_dir()
    def is_exists(self):
        return self.file_path.exists()

    def get_extension(self):
        return self.file_path.suffix[1:]