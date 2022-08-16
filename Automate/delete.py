import os
import sys

# ----------------------
# input arguments
# ----------------------
# -delete, delete containers

# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# read input argument
argument = len(sys.argv)
if (argument > 1):
    argument = sys.argv[1]

# if -delete input argument, delete containers
if(argument == 'delete'):
    delete('some-mysql')