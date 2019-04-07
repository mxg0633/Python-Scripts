import datetime
import os
import shutil
print('This Script will back up a valid source file path: ')
print('The program works by copying the input directory to a specified destination path: ')

source_path = input(' Please enter the source file path: ')
target_path = input(' Please enter the target file path: ')
shutil.copytree(source_path, target_path)

print('Back up Process Complete')