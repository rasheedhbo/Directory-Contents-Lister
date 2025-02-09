
# Directory Contents Lister

## About

**DirectoryContentsLister** is a simple tool designed to list and organize the contents of a selected directory on a Windows system. The application sorts files by type (with folders listed first) and saves the list to a `.txt` file. It's perfect for organizing and keeping track of files and subfolders in any directory.

---

## Installation

### Pre-built Executable:
You can download the latest `.exe` release from the [releases page](https://github.com/rasheedhbo/Directory-Contents-Lister/releases) and run it directly on Windows.

### From Source (Optional):
## Prerequisites
This tool requires Python 3.x. You can download the latest version of Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/rasheedhbo/Directory-Contents-Lister.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Directory-Contents-Lister
   ```
3. Optionally, create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
4. No additional dependencies are required, as the application relies on built-in Python libraries.

5. Run the program:
   ```bash
   python "DirectoryContentsLister.py"
   ```

---

## Usage

1. **Select a Directory**: When the program runs, you’ll be prompted to choose a folder whose contents you want to list.
2. **Choose Save Location**: The program will ask where to save the `.txt` file.
3. **Directory Listing**: The `.txt` file will contain a list of files and subfolders, sorted alphabetically, with folders appearing first.
4. **Open Folder Option**: After saving the `.txt` file, you’ll be asked if you want to open the folder where the file was saved.

---

## Updates in this Release

- **Initial Version**: First stable version of DirectoryContentsLister.
- **Bug Fixes**: Fixed sorting issues to ensure folders appear first in the listing.
- **UI Enhancements**: Custom icon added for a more professional appearance.

---

## Contributing

We welcome contributions! If you'd like to help, please fork the repository, create a branch, and submit a pull request. Feel free to open an issue for bugs or suggestions.

---

Feel free to contact me for any questions or support regarding this project!
