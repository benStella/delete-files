from genericpath import isfile
import re, fileinput, os, io

# REGEX for filter
file_name_regex = "(USA|Europe|World)"


# def myfunc():
# i = 0
# for i in EXCLUSIONS:
#     if i:
#         print("Hello")


def filter_names(file_names):
    # use the regex to filter files
    file_filter = re.search(file_name_regex, file_names)

    # filtered = filter(myfunc, file_names)
    # print(filtered)

    # If file contains words from filter, skip over file.
    # If file has no words from filter, delete file.
    if os.path.isfile(file_names):
        if file_filter:
            pass
        else:
            os.remove(file_names)
