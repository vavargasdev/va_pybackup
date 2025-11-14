"""
VaVar Backup - Backup/Sync Logic

@author: Vagner Vargas
@version: 0.2
@license: MIT
"""

import os
import shutil
from typing import List


class BackupManager:
    """Performs directory synchronization according to a given configuration."""

    @staticmethod
    def should_ignore(filename: str, ignore_list: List[str]) -> bool:
        """Return True if any ignore pattern is contained in filename."""
        for ign in ignore_list:
            if ign in filename:
                return True
        return False

    @staticmethod
    def sync_dirs(
        source_dir: str, dest_dir: str, exclude_dirs: List[str],
        ignore_files: List[str], update_existing: bool,
    ) -> int:
        """Synchronize source_dir -> dest_dir.
        Returns the number of processed files (count).
        """
        count = 0
        for root, dirs, files in os.walk(source_dir, followlinks=False):
            # filter excluded directories and symbolic links
            dirs[:] = [
                d for d in dirs
                if d not in exclude_dirs and not os.path.islink(os.path.join(root, d))
            ]

            for file in files:
                if BackupManager.should_ignore(file, ignore_files):
                    continue

                source_path = os.path.join(root, file)
                rel_path = os.path.relpath(source_path, source_dir)
                dest_path = os.path.join(dest_dir, rel_path)
                count += 1

                # ensure destination directory exists
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                # Check if file needs to be copied
                if not os.path.exists(dest_path):
                    print(f"Adding: {source_path}")
                    shutil.copy2(source_path, dest_path)
                elif update_existing and os.path.getmtime(source_path) > os.path.getmtime(dest_path):
                    print(f"Updating: {source_path}")
                    shutil.copy2(source_path, dest_path)
                else:
                    # This part is optional, but good for verbosity
                    print(f"Skipping: {source_path}")


        print(f"Total files processed: {count}")
        return count
