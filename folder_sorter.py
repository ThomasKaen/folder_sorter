import os
import shutil
import csv
from datetime import datetime

# --- Log File Name ---
LOG_FILE = "sort_log.csv"

# --- File Type Categories ---
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Spreadsheets": [".xlsx", ".csv"],
    "Scripts": [".py", ".js", ".sh"],
    "Archives": [".zip", ".rar", ".7z"]
}

# --- Determine Category ---
def get_category(file_ext):
    for category, extensions in FILE_CATEGORIES.items():
        if file_ext.lower() in extensions:
            return category
    return "Others"

# --- Sorting Function ---
def sort_files(folder_path):
    log_entries = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path):
            _, ext = os.path.splitext(filename)
            category = get_category(ext)
            dest_folder = os.path.join(folder_path, category)

            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            dest_path = os.path.join(dest_folder, filename)
            shutil.move(full_path, dest_path)

            log_entries.append([filename, category, datetime.now().isoformat()])

    return log_entries

# --- Write Log ---
def write_log(log_entries, folder_path):
    log_path = os.path.join(folder_path, LOG_FILE)
    with open(log_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(["Filename", "Category", "Moved At"])
        writer.writerows(log_entries)
    return log_path

# --- Main Entry Point ---
if __name__ == "__main__":
    print("=== Folder Sorter Script ===")
    target = input("Enter the full path of the folder you want to sort:\n> ").strip()

    if not os.path.exists(target):
        print("❌ Error: That folder does not exist. Please check the path.")
    else:
        print("📁 Sorting File....")
        entries = sort_files(target)
        log_file = write_log(entries, target)
        print(f"✅ Done! {len(entries)} files sorted.")
        print(f"📄 Log saved to: {log_file}")