from genericpath import isfile
import re, fileinput, os

# change this for file name regex name to delete
file_name_regex = "(Japan|Beta|Demo)"

# change this to directory of path of deletable files
dir_path = os.path.abspath("")
# change directory
os.chdir(dir_path)

# loop through filenames
for filename in os.listdir(dir_path):
    file_names = os.path.join(dir_path, filename)

    # use the regex to filter files
    file_filter = re.search(file_name_regex, file_names)

    # if path is a file and file matches regex then
    # delete the file
    if os.path.isfile(file_names):
        if file_filter:
            os.remove(file_names)
