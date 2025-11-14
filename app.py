"""
VaVar Backup - Tkinter GUI Application

@author: Vagner Vargas
@version: 0.2
@license: MIT
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import List

from config import BackupConfig
from manager import BackupManager


class BackupApp:
    """Tkinter GUI wrapper for managing configurations and running backups."""

    def __init__(self, config: BackupConfig):
        self.config = config
        self.root = tk.Tk()
        self.root.title("VaVar PyBackup")
        self.root.geometry("600x400")

        # Variables (English names)
        self.group_var = tk.StringVar()
        self.source_var = tk.StringVar()
        self.dest_var = tk.StringVar()
        self.exclude_var = tk.StringVar()
        self.ignore_var = tk.StringVar()
        self.update_var = tk.BooleanVar()
        self.notes_var = tk.StringVar()

        self._build_ui()

    def _build_ui(self) -> None:
        """Create and layout the UI elements."""
        frm = ttk.Frame(self.root, padding=10)
        frm.grid(row=0, column=0, sticky="nsew")

        # expansion config
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        frm.grid_columnconfigure(1, weight=1)
        frm.grid_rowconfigure(6, weight=1)

        tk.Label(frm, text="Configuration Group:").grid(row=0, column=0, sticky="w")
        self.group_dropdown = ttk.Combobox(
            frm, textvariable=self.group_var, values=self.config.groups()
        )
        self.group_dropdown.grid(row=0, column=1, sticky="we")
        self.group_dropdown.bind("<<ComboboxSelected>>", lambda e: self.load_group())

        tk.Label(frm, text="Source Directory:").grid(row=1, column=0, sticky="w")
        tk.Entry(frm, textvariable=self.source_var).grid(row=1, column=1, sticky="we")

        tk.Label(frm, text="Destination Directory:").grid(row=2, column=0, sticky="w")
        tk.Entry(frm, textvariable=self.dest_var).grid(row=2, column=1, sticky="we")

        tk.Label(frm, text="Directories to Exclude (comma-separated):").grid(
            row=3, column=0, sticky="w"
        )
        tk.Entry(frm, textvariable=self.exclude_var).grid(row=3, column=1, sticky="we")

        tk.Label(frm, text="Files to Ignore (comma-separated):").grid(
            row=4, column=0, sticky="w"
        )
        tk.Entry(frm, textvariable=self.ignore_var).grid(row=4, column=1, sticky="we")

        tk.Label(frm, text="Update Existing Files:").grid(row=5, column=0, sticky="w")
        tk.Checkbutton(frm, variable=self.update_var).grid(row=5, column=1, sticky="w")

        tk.Label(frm, text="Notes:").grid(row=6, column=0, sticky="nw")
        self.text_area = tk.Text(frm, wrap="word", height=10)
        self.text_area.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)

        tk.Button(frm, text="Save Configuration", command=self.save_group).grid(
            row=7, column=0, sticky="we"
        )
        tk.Button(frm, text="Start Backup", command=self.start_backup).grid(
            row=7, column=1, sticky="we"
        )

    def load_group(self) -> None:
        """Load configuration into UI fields for the selected group."""
        group = self.group_var.get()
        conf = self.config.get_group(group)
        self.source_var.set(conf["source_dir"])
        self.dest_var.set(conf["dest_dir"])
        self.exclude_var.set(",".join(conf["exclude_dirs"]))
        self.ignore_var.set(",".join(conf["ignore_files"]))
        self.update_var.set(conf["update_existing"])
        self.notes_var.set(conf["notes"])
        # update text area manually
        self.text_area.delete("1.0", "end")
        self.text_area.insert("1.0", conf["notes"])

    def save_group(self) -> None:
        """Save current UI state as a configuration group."""
        group = self.group_var.get().strip()
        if not group:
            messagebox.showerror("Error", "Group name cannot be empty.")
            return

        notes = self.text_area.get("1.0", "end").strip()

        def clean_list(text: str) -> List[str]:
            return [item.strip() for item in text.split(",") if item.strip()]

        conf = {
            "source_dir": self.source_var.get().strip(),
            "dest_dir": self.dest_var.get().strip(),
            "exclude_dirs": clean_list(self.exclude_var.get()),
            "ignore_files": clean_list(self.ignore_var.get()),
            "update_existing": self.update_var.get(),
            "notes": notes,
        }

        self.config.save_group(group, conf)
        # refresh combobox values
        self.group_dropdown["values"] = self.config.groups()
        messagebox.showinfo("Success", "Configuration saved successfully!")

    def start_backup(self) -> None:
        """Read selected group configuration and run synchronization."""
        group = self.group_var.get()
        conf = self.config.get_group(group)

        if not conf["source_dir"] or not conf["dest_dir"]:
            messagebox.showerror("Error", "Source and destination directories must be configured.")
            return

        # Remove 'notes' as it's not an argument for sync_dirs
        sync_args = {k: v for k, v in conf.items() if k != 'notes'}

        count = BackupManager.sync_dirs(**sync_args)
        messagebox.showinfo("Completed", f"Backup finished!\n{count} files processed.")

    def run(self) -> None:
        """Start the Tkinter main loop."""
        self.root.mainloop()
    