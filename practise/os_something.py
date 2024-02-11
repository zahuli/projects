import os
import sys


# This line gets the current working directory (CWD)
directory = os.getcwd()

print(directory)

# os.path.join() method in Python join one or more path components intelligently. This method concatenates various path components with exactly one directory separator (‘/’) following each non-empty part except the last path component. If the last path component to be joined is empty then a directory separator (‘/’) is put at the end.

print(os.path.join(os.getcwd(), "models", "model-a", "v1", "list"))

os.makedirs(os.path.join(os.getcwd(), "models",
            "model-a", "v1", "list"), exist_ok=True)
