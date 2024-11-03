from pathlib import Path
import shutil

def move_file(file_path:Path,target_dir:Path)->None:
    shutil.move(str(file_path), target_dir / file_path.name)
