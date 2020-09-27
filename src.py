import os
import sys

def count_py_files(dirname):
    if os.path.exists(os.path.join(dirname, '.git')):
        count = 0
        for root, dirs, files in os.walk(dirname):
            count += len([f for f in files if f.endswith('.py')])
        print(f'{dirname} has {count} Python files')
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isdir(path):
            count_py_files(path)

def distill_py_file(orig='orig.py', dest='dest.py'):
    with open(orig, 'r') as file:
        lines = file.readlines()    
    lines = [line for line in lines if line!='\n']
    lines = [line for line in lines if not line.strip().startswith('#')]
    lines = [line for line in lines if len(line.split('"""'))!=3]    
    output, count = [], 0
    for line in lines:
        if line.strip()[:3] == '"""':
            count += 1
        else: 
            if count%2 == 0: 
                output.append(line)    
    with open(dest, 'w') as file:
        for line in output:
            file.write(line)            
            
if __name__ == '__main__':
    count_py_files('./github')
