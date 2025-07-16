import os
directory = '/etc'  # Path to the directory
for file in os.listdir(directory):  # Loop through files in the directory
    if file.endswith('.conf'):
        print(file)
      

# To print full paths and only files (skip subdirectories)
for file in os.listdir(directory):
    full_path = os.path.join(directory, file)
    if file.endswith('.conf') and os.path.isfile(full_path):
        print(full_path)

      
# Alternative: Using glob (Cleaner)
import glob

for file in glob.glob('/etc/*.conf'):
    print(file)
