import os
import re

# Replace path with the directory to search for files
directory = '/path/to/your/directory'

# Define the words you want to search for within parentheses
word_filter = ['word1', 'word2', 'word3']

# Function to filter and delete files
def delete_files(directory, word_filter):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # Extracts text within parentheses
            match = re.search(r'\((.*?)\)', filename)
            if match:
                text_inside_parentheses = match.group(1)
                # Check if filter matches text inside parentheses
                if not any(word in text_inside_parentheses for word in word_filter):
                    file_path = os.path.join(directory, filename)
                    # >>> !!! Comment out below line to delete file !!! <<<
                    # os.remove(file_path)
                    print(f"Deleted: {filename}")

# Call the function to delete files
delete_files(directory, word_filter)
