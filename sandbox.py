import os
try:
    print(os.environ['PYTHONPATH'].split(os.pathsep))
except KeyError:
    user_paths = []