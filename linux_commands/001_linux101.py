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
