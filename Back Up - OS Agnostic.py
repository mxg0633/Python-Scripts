import datetime
import os
import shutil
from pathlib import Path

print('This Script will back up a valid source file path: ')
print('The program works by copying the input directory to a specified destination path: ')

source_path = Path(input(' Please enter the source c:file path: '))
if not source_path.exists():
     print('Oops, source path provided does not exist!')

else: print('The source path is valid. Proceeding in copying files process... ')
target_path = Path(input(' Please enter the target file path: '))
if not target_path.exists():
     print('Oops, the destination path provided does not exist!')
     makenew = input('Would you like to create the missing directory: True or False?')
     if makenew == (True):
      shutil.rmtree(target_path)
     os.makedirs(target_path)
     shutil.copytree(source_path, target_path)
     if makenew == (False):
      print('Back up Process Canceled')
else:
        print('The destination path is valid. Copying files... ')
        shutil.rmtree(target_path)
        shutil.copytree(source_path, target_path)

print('Back up Process Complete')