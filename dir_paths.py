from genericpath import isfile
import re, fileinput, os

from filter import filter_names


def paths():
    # directory path
    dir_path = os.path.abspath("/home/bens-desktop/Desktop/roms/Sega - Game Gear")

    # change directory
    os.chdir(dir_path)

    # loop through filenames
    for filename in os.listdir(dir_path):
        file_names = os.path.join(dir_path, filename)
        file_names = filter_names(file_names)
