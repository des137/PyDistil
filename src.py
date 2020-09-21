import os
import sys

def count_py_files(dirname):
  if os.path.exists(os.path.join(dirname, '.git')):
    count = 0
    for root, dirs, files in os.walk(dirname):
      count += len([f for f in files if f.endswith('.py')])
    print(f'{dirname} has {count} Python files')
  for name in os.listdir(dirname):
    path = os.path.join(dirname, name):
      if os.path.isdir(path):
        count_py_files(path)
