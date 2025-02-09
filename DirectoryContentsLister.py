import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
from collections import defaultdict

# Function to list contents of the chosen directory and save to a file
def list_directory_contents(directory_path, save_path):
    try:
        # Extract the folder name from the directory path
        folder_name = os.path.basename(directory_path.rstrip(os.sep))
        
        # Get the list of files and folders in the directory
        contents = os.listdir(directory_path)
        
        # Separate folders and files by type
        folders = []
        files_by_type = defaultdict(list)
        
        for item in contents:
            # Get the full path of the item
            full_item_path = os.path.join(directory_path, item)
            
            # Check if the item is a folder
            if os.path.isdir(full_item_path):
                folders.append(item)
            else:
                # Get the file extension and group by type (use .extension as the key)
                _, ext = os.path.splitext(item)
                ext = ext.lower()  # Normalize to lowercase
                files_by_type[ext].append(item)
        
        # Sort folders alphabetically
        folders.sort()
        
        # Sort file types (extensions) alphabetically
        sorted_file_types = sorted(files_by_type.keys())
        
        # Create the output file name if save_path is not provided
        if not save_path:
            save_path = f"{folder_name}_contents.txt"
        
        # Open the file to write the contents with utf-8 encoding
        with open(save_path, 'w', encoding='utf-8') as file:
            # Write folders first (only if there are files or other folders to be listed)
            if folders and (files_by_type or folders):  # Include folders only if there are files or folders
                for folder in folders:
                    file.write(folder + "\n" if len(folders) == len(contents) else folder + " (Folder)\n")
            
            # Write files grouped by type
            for ext in sorted_file_types:
                # Sort files by name within each extension group
                files_by_type[ext].sort()
                # Write the group header (file extension)
                file.write(f"--- {ext.upper()} Files ---\n")
                for file_item in files_by_type[ext]:
                    file.write(file_item + '\n')
        
        # Show a success message
        messagebox.showinfo("Success", f"Contents of '{directory_path}' have been saved to '{save_path}'")

        # Ask the user if they want to open the folder
        if messagebox.askyesno("Open Folder", f"Do you want to open the folder where the file was saved?"):
            # Get the folder path of the saved .txt file
            folder_path = os.path.dirname(save_path)  # Ensure we use the latest save path
            
            # Open the folder containing the saved .txt file
            folder_path = folder_path.replace("/", "\\")  # Replace slashes with backslashes for Windows
            subprocess.Popen(f'explorer "{folder_path}"')  # Open the folder directly
        else:
            # Go back to the home screen (main Tkinter window)
            root.deiconify()  # Show the main window again if it's minimized

    except FileNotFoundError:
        messagebox.showerror("Error", f"The directory '{directory_path}' was not found.")
    except PermissionError:
        messagebox.showerror("Error", f"You do not have permission to access '{directory_path}'.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to open the directory dialog and process the directory
def open_directory():
    # Hide the main window while processing
    root.iconify()  # Hide the main window (minimize)
    
    # Ask the user to select a folder
    directory_path = filedialog.askdirectory(title="Select a Directory")
    
    if directory_path:
        # Ask the user where to save the text file
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")],
                                                 initialfile=os.path.basename(directory_path) + "_contents.txt",
                                                 title="Save Directory Contents")
        
        if save_path:  # Proceed only if the user selected a save path
            # Call the function to list directory contents and save to file
            list_directory_contents(directory_path, save_path)

# Create the main Tkinter window
root = tk.Tk()
root.title("Directory Contents Lister")

# Set the window size
root.geometry("400x200")

# Set the window icon (path to your .ico file)
root.iconbitmap("C:/Users/RASHEED/folderapp/icon.ico")

# Add a button to open the directory dialog
button = tk.Button(root, text="Select Directory", command=open_directory)
button.pack(pady=50)

# Start the Tkinter event loop
root.mainloop()
