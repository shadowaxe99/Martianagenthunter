```python
from PIL import Image

def open_image(file_path):
    try:
        img = Image.open(file_path)
        return img
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

def save_image(img, file_path):
    try:
        img.save(file_path)
        print("Image saved successfully.")
    except Exception as e:
        print(f"Error saving image: {e}")

def resize_image(img, size):
    try:
        resized_img = img.resize(size)
        return resized_img
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None

def rotate_image(img, angle):
    try:
        rotated_img = img.rotate(angle)
        return rotated_img
    except Exception as e:
        print(f"Error rotating image: {e}")
        return None

def crop_image(img, box):
    try:
        cropped_img = img.crop(box)
        return cropped_img
    except Exception as e:
        print(f"Error cropping image: {e}")
        return None
```