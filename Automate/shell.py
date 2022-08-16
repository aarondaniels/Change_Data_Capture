import os
import sys

# ------------------
# input arguments
# ------------------
# -list, list files
# -listHidden, list hidden files

# list files
def list_files():
    cmd = f'ls -l'
    result = os.system(cmd)
    print(result)

def list_hidden_files():
    cmd = f'ls -ls'
    result = os.systm(cmd)
    print(result)

#read input arguments
argument = len(sys.argv)
if (argument > 1):
    argument =sys.argv[1]

#if -list list files
if(argument == '-list'):
    list_files()

#if -list list hiddenfiles
if(argument == '-listHidden'):
    list_hidden_files()

# Execute by entering `python3 shell.py -list` in command line