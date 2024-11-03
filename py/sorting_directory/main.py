from pathlib import Path

def create_dir(str_path):
    """create directory if it doesn't exist'"""
    Path(str_path).mkdir(exist_ok=True)