```python
import os
import shutil
from security.user_consent import get_user_consent

def edit_file(filepath, new_content):
    consent = get_user_consent()
    if consent:
        with open(filepath, 'w') as file:
            file.write(new_content)
        return True
    else:
        return False

def move_file(source_filepath, destination_filepath):
    consent = get_user_consent()
    if consent:
        shutil.move(source_filepath, destination_filepath)
        return True
    else:
        return False

def copy_file(source_filepath, destination_filepath):
    consent = get_user_consent()
    if consent:
        shutil.copy2(source_filepath, destination_filepath)
        return True
    else:
        return False

def delete_file(filepath):
    consent = get_user_consent()
    if consent:
        os.remove(filepath)
        return True
    else:
        return False
```