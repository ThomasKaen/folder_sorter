# 🗂️ Folder Sorter – Python Script to Organize Files by Type

A simple, customizable Python script that automatically sorts files in a folder into subfolders based on file type (e.g., `.jpg` → `Images`, `.pdf` → `Documents`, etc.).

Perfect for cleaning up your Downloads folder, organizing workspaces, or automating routine file sorting.

---

## 💡 Features

- Automatically sorts files by extension into logical categories
- Creates folders on-the-fly if they don’t exist
- Logs every move in a clean `.csv` file
- Cross-platform: works on Windows, macOS, and Linux
- No coding experience required — just paste a folder path and go

---

## 🚀 How to Use

### 1. Install Python  
If you don’t have Python yet, download it here:  
👉 https://www.python.org/downloads/

### 2. Run the Script  
Open your terminal or command prompt and run:

```bash
python folder_sorter.py
```

Paste the **full path to the folder** you want to organize when prompted.

That’s it! The script will sort files and generate a log file called `sort_log.csv`.

---

## 🗃️ Example Folder Structure

**Before:**

```
Downloads/
├── image1.jpg
├── resume.pdf
├── script.py
├── notes.txt
```

**After:**

```
Downloads/
├── Images/
│   └── image1.jpg
├── Documents/
│   └── resume.pdf
├── Scripts/
│   └── script.py
├── Others/
│   └── notes.txt
├── sort_log.csv
```

---

## ⚙️ Customize File Categories

You can edit the `FILE_CATEGORIES` dictionary at the top of the script to match your needs:

```python
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Spreadsheets": [".xlsx", ".csv"],
    "Scripts": [".py", ".js", ".sh"],
    "Archives": [".zip", ".rar", ".7z"]
}
```

Any file that doesn’t match a listed extension will go into the `Others/` folder.

---

## 🧑‍💻 Created By

**Tamas Kiss**  
Python developer & automation specialist  
> 💼 Hire me to build your custom scripts or automations on [Fiverr](#)

---

## 🛠️ Need Custom Features?

This script can be modified for:
- Sorting by **file size**, **creation date**, or **name**
- Filtering specific file types
- Running automatically on a schedule
- Creating daily backup folders

📩 Just reach out if you’d like a custom version.

---
