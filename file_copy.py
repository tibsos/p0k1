import os
import shutil
import tkinter as tk
from tkinter import messagebox

def delete_files_in_directory(directory):
    try:
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            try:
                os.remove(file_path)
            except PermissionError:
                print(f"Permission denied for {file_path}")
    except Exception as e:
        print(f"Error accessing {directory}: {e}")

def prefetch():
    delete_files_in_directory(r'/System/Library/Caches')

def temp():
    delete_files_in_directory(r'/private/var/tmp')

def find_file():
    search_term = entry.get()
    if not search_term:
        messagebox.showinfo("Input Error", "Please enter a file or folder name.")
        return
    for root, dirs, files in os.walk(r'/'):
        for name in dirs + files:
            if name == search_term:
                entry.delete(0, tk.END)
                entry.insert(tk.END, os.path.join(root, name))
                return
    messagebox.showinfo("Search Result", "File or folder not found.")

def copy_item():
    source = entry.get()
    destination = r'/Users/YourUsername/Desktop/NewFolder'
    try:
        if os.path.isdir(source):
            shutil.copytree(source, destination)
        elif os.path.isfile(source):
            shutil.copy(source, destination)
        else:
            messagebox.showinfo("Copy Error", "Invalid source path.")
    except Exception as e:
        print(f"Error copying: {e}")

root = tk.Tk()
root.title("File Utility")
root.geometry("400x300")
root.configure(bg="gray")

# Entry Field with improved visibility
entry = tk.Entry(root, width=50, bg="white", fg="black", font=("Helvetica", 12), relief="solid")
entry.pack(pady=10)

root.configure(bg="white")
entry = tk.Entry(root, bg="lightgray", fg="black")
entry.pack(padx=10, pady=10)


# Buttons
tk.Button(root, text="Clear Caches", command=prefetch, bg="blue", fg="white", font=("Helvetica", 10)).pack(pady=5)
tk.Button(root, text="Clear Temp", command=temp, bg="blue", fg="white", font=("Helvetica", 10)).pack(pady=5)
tk.Button(root, text="Find File/Folder", command=find_file, bg="blue", fg="white", font=("Helvetica", 10)).pack(pady=5)
tk.Button(root, text="Copy File/Folder", command=copy_item, bg="blue", fg="white", font=("Helvetica", 10)).pack(pady=5)

root.mainloop()