# OS module
from datetime import datetime
import os
# print(dir(os))

# current working dir >>>>>>>>>>>>>>
cwd = "/Users/hq2nguye/Desktop/DailyCoding/self_python"
print(os.getcwd())

# Change working dir >>>>>>>>>>>>>>
# os.chdir("/Users/hq2nguye/Desktop/DailyCoding/")
# print(os.getcwd()) # --> "/Users/hq2nguye/Desktop/DailyCoding/"

# Check whats inside: >>>>>>>>>>>>>>
print(os.listdir(cwd))

# Create new folder:
os.mkdir("os_mkdir_test")  # create one folder at a time
os.makedirs("os_makedirs_test/os_mkdir")  # create super folder and sub folers: MORE CONVENIENT TO CREATE

# Remove folders: >>>>>>>>>>>>>>
os.rmdir("os_mkdir_test")  # remove one folder at a time: SAFER TO USE THIS WHEN REMOVE
os.removedirs("os_makedirs_test/os_mkdir")  # remove super folder and sub folers

print(os.listdir(cwd))

# Rename file and folders: >>>>>>>>>>>>>>
os.makedirs("test.txt")
os.rename("test.txt", "test_rename.txt")
print(os.listdir(cwd))

# Get infomation about a file: >>>>>>>>>>>>>>
print(os.stat("001_better_code.py"))
print(os.stat("001_better_code.py").st_size)  # get the file's size in bytes
modification_time = os.stat("001_better_code.py").st_mtime
print(datetime.fromtimestamp(modification_time))

# View the whole directory tree >>>>>>>>>>>>>>
print(os.walk(cwd))  # generator that yield a tuple with 3 values (path, dirs in the path, files in path)
# by default it traverse from top down
for dirpath, dirnames, filenames in os.walk(cwd):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)  # folders
    print("Files: ", filenames)  # files
    print()

# Getting environemt >>>>>>>>>>>>>>
# print(os.environ)
print(os.environ.get("HOME"))

# join the path w/ the file WITHOUT messing up the slash >>>>>>>
filepath = os.path.join(os.environ.get("HOME"), "test.txt")
print(filepath)

# Get basename & dirname: the file path does not have to exist to work >>>>>>
print(os.path.basename("/Users/hq2nguye/test.txt"))  # test --> useful
print(os.path.dirname("/Users/hq2nguye/test.txt"))  # /Users/hq2nguye --> useful
print(os.path.split("/Users/hq2nguye/test.txt"))  # ('/Users/hq2nguye', 'test.txt') --> useful

# Check if path exist: >>>>>>>>>
print(os.path.exists("/Users/hq2nguye/test.txt"))  # False

# Check if it is a file or a dir >>>>>>>>>
print(os.path.isfile(cwd))  # False: /Users/hq2nguye/Desktop/DailyCoding/self_python is NOT a file
print(os.path.isdir(cwd))  # True: /Users/hq2nguye/Desktop/DailyCoding/self_python is a dir (folder)

# Split the extension: csv, pdf of a file >>>>>>>
print(os.path.splitext("/Users/hq2nguye/Desktop/DailyCoding/self_python/006_os_module.py"))
# ('/Users/hq2nguye/Desktop/DailyCoding/self_python/006_os_module', '.py')
