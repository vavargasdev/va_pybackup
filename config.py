"""
VaVar Backup - Configuration Management

@author: Vagner Vargas
@version: 0.2
@license: MIT
"""

import os
import json
from typing import Dict, List

CONFIG_FILE = "backup_config.json"


class BackupConfig:
    """Manage loading and saving backup configurations to a JSON file.
    Configurations are stored as a dict mapping group name -> configuration dict.
    Configuration dict keys: source_dir, dest_dir, exclude_dirs,
    ignore_files, update_existing, notes
    """

    def __init__(self, path: str = CONFIG_FILE):
        self.path = path
        self._data: Dict[str, Dict] = {}
        self._load()

    def _load(self) -> None:
        """Load configuration file if exists, otherwise initialize empty dict."""
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as f:
                self._data = json.load(f)
        else:
            self._data = {}

    def save_group(self, group: str, config: Dict) -> None:
        """Save or update a group configuration and flush to disk."""
        self._data[group] = config
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=4, ensure_ascii=False)

    def get_group(self, group: str) -> Dict:
        """Return configuration for group or a default template."""
        return self._data.get(
            group,
            {
                "source_dir": "", "dest_dir": "", "exclude_dirs": [],
                "ignore_files": [], "update_existing": True, "notes": "",
            },
        )

    def groups(self) -> List[str]:
        """Return a list of saved group names."""
        return list(self._data.keys())
