```python
import os
import shutil
from security.user_consent import get_user_consent

def create_folder(path):
    try:
        if get_user_consent():
            os.makedirs(path)
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred while creating the folder: {e}")
        return False

def delete_folder(path):
    try:
        if get_user_consent():
            shutil.rmtree(path)
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred while deleting the folder: {e}")
        return False

def move_folder(source_path, destination_path):
    try:
        if get_user_consent():
            shutil.move(source_path, destination_path)
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred while moving the folder: {e}")
        return False

def copy_folder(source_path, destination_path):
    try:
        if get_user_consent():
            shutil.copytree(source_path, destination_path)
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred while copying the folder: {e}")
        return False
```