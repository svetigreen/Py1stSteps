import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText


def open_file():
    # Open the file dialog and get the file path
    file_path = filedialog.askopenfilename(title="Select a file",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    if file_path:
        try:
            # Open the file and read the content
            with open(file_path, "r") as file:
                content = file.read()

            # Clear the current content in the ScrolledText widget
            text_area.delete(1.0, tk.END)

            # Insert the file content into the ScrolledText widget
            text_area.insert(tk.INSERT, content)

            # Display the file path in the title
            root.title(f"File Explorer Example - {file_path}")

        except Exception as e:
            # Display an error message in case of failure
            messagebox.showerror("Error", f"Unable to open file: {e}")


def save():
    # Open the save dialog to get the file path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get('1.0', END))


# Create the main window
root = tk.Tk()
root.title("File Explorer Example")
# root.geometry("600x400")

# Add a button to open the file explorer
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=10)

# Create a ScrolledText widget for displaying file content
text_area = ScrolledText(root, wrap=tk.WORD, width=70, height=20)
text_area.pack(pady=10)

# Add a button to save the contents
Button(text='Save', command=save).pack(pady=10)

# Run the application
root.mainloop()
