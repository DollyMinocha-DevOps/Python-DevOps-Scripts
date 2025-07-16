# Write a loop to print all files ending with .log in /var/log.

import os
for file in os.listdir('/var/log'):
  if file.endswith('.log'):
    print(file)

# OS Module gives access to OS-Level operations, here we use it to list directory contents (os.listdir)
# and perform file system checks

import os
for file in os.listdir('/var/log') and os.path.isfile(os.path.join('/var/log', file):
  if file.endswith('.log'):
    print(file)
    
# os.path to filter only files (skip directories)

import glob
for file in glob.glob('/var/log/*.log'):
  print(file)

# glob module is a part of Pythin's standard library. It is used for pattern matching in file paths, similar to shell wildcards. 
# *.log matches all the files ending in .log
# glob.glob('/var/log/*.log') returns a list of all files in /var/log whose names end with .log
# No need for manual filtering like endswith('.log'). It directly matches patterns.
