import os
import re
import PySimpleGUI as sg


# sg.popup_get_folder("Choose a folder")
folder_input = sg.popup_get_folder("Select folder to delete files")

# Define the words you want to search for within parentheses
word_filter = ["USA", "Europe", "World"]
delete_list = ["Unl", "Demo", "Auto Demo"]


# Function to filter and delete files
def delete_files(folder_input, word_filter):
    for filename in os.listdir(folder_input):
        if os.path.isfile(os.path.join(folder_input, filename)):
            # Extracts text within parentheses
            match = re.search(r"\((.*?)\)", filename)
            if match:
                text_inside_parentheses = match.group(1)
                # Check if filter matches text inside parentheses

                if any(word in text_inside_parentheses for word in delete_list):
                    file_path = os.path.join(folder_input, filename)
                    # os.remove(file_path)
                    print(f"Deleted: {filename}")

                # elif not any(word in text_inside_parentheses for word in word_filter):
                #     file_path = os.path.join(folder_input, filename)
                # >>> !!! Comment out below line to delete file !!! <<<
                # os.remove(file_path)
                # print(f"Deleted: {filename}")


# Call the function to delete files
delete_files(folder_input, word_filter)
