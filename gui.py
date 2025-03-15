import tkinter as tk
from tkinter import messagebox
from db import WeebDB

class WeebGUI:
    def __init__(self, root):
        """Initialize the GUI components"""
        self.db = WeebDB()

        root.title("Anime Entry Form")
        root.geometry("350x200")

        tk.Label(root, text="Anime Name:").pack()
        self.entry_name = tk.Entry(root, width=30)
        self.entry_name.pack()

        tk.Label(root, text="Release Date (YYYY-MM-DD):").pack()
        self.entry_date = tk.Entry(root, width=30)
        self.entry_date.pack()

        tk.Label(root, text="OTT Platform:").pack()
        self.entry_ott = tk.Entry(root, width=30)
        self.entry_ott.pack()

        submit_button = tk.Button(root, text="Submit", command=self.save_to_db)
        submit_button.pack()

    def save_to_db(self):
        """Save the user input to MongoDB"""
        anime_name = self.entry_name.get()
        release_date = self.entry_date.get()
        ott_platform = self.entry_ott.get()

        if anime_name and release_date and ott_platform:
            self.db.insert_anime(anime_name, release_date, ott_platform)
            messagebox.showinfo("Success", "Anime details saved successfully!")
            self.entry_name.delete(0, tk.END)
            self.entry_date.delete(0, tk.END)
            self.entry_ott.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All the fields are required!")