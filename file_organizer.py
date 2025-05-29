import os
import shutil
from tkinter import Tk, Button, Label, filedialog, messagebox
from datetime import datetime

def organize_by_type(folder_path):
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            ext = os.path.splitext(filename)[1].lower().strip('.')
            if not ext:
                ext = 'no_extension'
            target_dir = os.path.join(folder_path, ext)
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(full_path, os.path.join(target_dir, filename))
    messagebox.showinfo("Done", "Organized files by type!")

def organize_by_date(folder_path):
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            timestamp = os.path.getmtime(full_path)
            date_str = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
            target_dir = os.path.join(folder_path, date_str)
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(full_path, os.path.join(target_dir, filename))
    messagebox.showinfo("Done", "Organized files by date!")

def organize_by_custom(folder_path):
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            if filename.lower().startswith('report'):
                target_dir = os.path.join(folder_path, 'Reports')
            else:
                target_dir = os.path.join(folder_path, 'Others')
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(full_path, os.path.join(target_dir, filename))
    messagebox.showinfo("Done", "Organized files by custom rule!")

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_label.config(text=folder)
        global selected_folder
        selected_folder = folder

root = Tk()
root.title("File Organizer")

selected_folder = ""

Label(root, text="Select folder to organize:").pack(pady=5)
folder_label = Label(root, text="No folder selected", fg="blue")
folder_label.pack(pady=5)

Button(root, text="Select Folder", command=select_folder).pack(pady=5)
Button(root, text="Organize by Type", command=lambda: organize_by_type(selected_folder) if selected_folder else messagebox.showerror("Error", "Please select a folder")).pack(pady=5)
Button(root, text="Organize by Date", command=lambda: organize_by_date(selected_folder) if selected_folder else messagebox.showerror("Error", "Please select a folder")).pack(pady=5)
Button(root, text="Organize by Custom Rule", command=lambda: organize_by_custom(selected_folder) if selected_folder else messagebox.showerror("Error", "Please select a folder")).pack(pady=5)

root.geometry("300x250")
root.mainloop()
