import os
try: 
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
    print(sys.path)
except KeyError:
    user_paths = []
