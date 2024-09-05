from subprocess import Popen, PIPE
import os

# Construct the file path for your HTML file
path = 'messy.html'

# Read the HTML content from the file
with open(path, 'r', encoding='utf-8') as file:
    text = file.read()

# Run the 'tidy' command as a subprocess
try:
    tidy = Popen(['tidy', '-q', '-i'], stdin=PIPE, stdout=PIPE, stderr=PIPE)

    # Send the HTML content to tidy, and get the output and errors
    stdout_data, stderr_data = tidy.communicate(input=text.encode())

    # Print the tidied HTML output (stdout)
    print(stdout_data.decode())

    # Print any error messages (stderr)
    if stderr_data:
        print("Tidy Error Output:")
        print(stderr_data.decode())

except FileNotFoundError as e:
    print(f"Error: {e}. 'tidy' not found in the system PATH.")
except Exception as e:
    print(f"An error occurred: {e}")
