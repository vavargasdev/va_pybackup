"""
VaVar Backup - Simple backup/sync system

@author: Vagner Vargas
@version: 0.2
@license: MIT
"""

from app import BackupApp
from config import BackupConfig


def main() -> None:
    """Entry point: instantiate config and app, then run."""
    cfg = BackupConfig()
    app = BackupApp(cfg)
    app.run()

if __name__ == "__main__":
    main()
