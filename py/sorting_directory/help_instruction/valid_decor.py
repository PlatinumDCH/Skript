from pathlib import Path
import functools
from errors.specific import  NotExists, NotIsDirectory


def check_directory(func):
    @functools.wraps(func)
    def wrapper(path:str,*args, **kwargs):
        directory_path = Path(path)
        if not directory_path.is_dir():
            raise NotIsDirectory('f"The specified path does not exist: {path}"')
        if not directory_path.exists():
            raise NotExists('f"The specified path does not exist"')
        return func(path, *args, **kwargs)
    return wrapper()

