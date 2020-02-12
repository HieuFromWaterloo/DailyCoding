# >>>>>>>> WORKING WITH FILES <<<<<<<<<<

# Search for mannual
man cp  # this will show all the instruction

# cd : change dir
cd ..  # MOVE UP 1 DIRECTORY
cd .. / ..

# ls -la: list all hidden files in long form

# ls -a: list all hidden files in short form

# mkdir: create dir

# touch: create file
touch textfile.txt

# cp textfile.txt: create a copy file

# mv textfile.txt textfile_name_change.txt: moving files and rename files are pretty much the same

# mv textfile.txt SubDir1/ : move file into a folder
mv textfile_name_change.txt .. / original.txt  # move up 1 dir AND rename at the same time

# rm file.txt
# BE VERY CAREFUL: because rm file on the system cannot be recovered

# >>>>>>> WORKING WITH DIRECTORIES <<<<<<<<<
# create a copy of a dir
mkdir CopyDir
# USE -R for directory
cp - R Directory / CopyDir/

# the rest like "mv" can be used without -R

# Remove Directory
rm - R CopyDir/

# FORCE DELETE--- CAREFULE
rm - rf TesterDir/

# >>>>>>>>>>>>> FIND <<<<<<<<<<<<<<<<<<<<<<
man find

# find all file in CURRENT directory
find .

# find all file in a directory
find MyWebsite

# Only find the directory BUT IGNORE all the files in CURRENT dir
find . -type d

#-- EXACT SEARCH for a file name within current dir
find . -type f - name "test_file.txt"

#-- * SEARCH for a file name within current dir
find . -type f - name "test*"

#-- NOTE here -name is CASE SENSITIVE

#-- * SEARCH NON CAST SENSITIVE - iname
find . -type f - iname "test*"

# * SEARCh for all .py files
find . -type f - iname "*.py"

#-- Find all files being modified in LESS THAN 10 mins ago
find . -type f - mmin - 10

# Find all files being modified in MORE THAN 10 mins ago
find . -type f - mmin + 10

#-- Find all files being modified in MORE THAN 1 mins AND LESS THAN 5 mins
find . -type f - mmin + 1 - mmin - 5

# Find all files being modified in LEST THAN 10 DAYS ago: -mtime
find . -type f - mtime 20  # less than 20 days ago

"""
- mmin, mtime: modified min and day
- cmin, ctime: changed min and day
- amin, atime: accessed min and day
"""

# -- Search by file size
# find all the files more than 5MB
find . -size + 5M  # OR 5k, 5G

# check file size
ls - lah

#-- Search for Empty files
find . -empty

#-- Search file with permission 777
find . -perm 777

# >>>>>>>>>>>>> Perform action on search result <<<<<<<<<<<<
find . -perm 777
# Now everything is set to 777, which gives every one the permission to:
# read, write and execute permissions

"""
1. first, change the user name and group for every directory and file in our folder

2. then, set all the DIR to have permission level of 775 and all the file to FILES to have permission level of 664

-exec: exucute
-chown: change owner
"""

# 1-- change user and gorup
find MyWebsite - exec chown hq2nguye: www - data {} +  # added placeholder "{}" for all the result and "+" to end the command
# check the result
ls - la

# 2-- set all the DIR to have permission level of 775
find MyWebsite - type d - exec chmod 775 {} +
# check the result
find MyWebsite - perm 775

# all the file to FILES to have permission level of 664
find MyWebsite - type f - exec chmod 664 {} +
find MyWebsite - perm 664

# >>>>>>>>>>> DELETE ALL *.JPG FILES <<<<<<<<<<
"""
1. ALways Search "*.jpg" before remove to see whats there
find . -type -f -name "*.py"

2. Sometimes we ONLY wanna remove files from CURRENT dir, NOT from the subdir
--> use -maxdepth 1
"""

# -- REMOVE all .jpg files in current dir
find . -type f - name "*.jpg" - maxdepth 1 - exec rm {} +
