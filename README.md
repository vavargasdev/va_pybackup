<div align="right">
<a href="./README-pt.md">Ler em português</a>
</div>

# VaVargas PyBackup - Simple Backup Manager

A simple desktop application built with Python and Tkinter to manage and execute file backup/synchronization tasks.

![VaVar PyBackup](https://raw.githubusercontent.com/vavargasdev/va_pybackup/refs/heads/main/VaVarBackupScreen.jpg)

## Features

-   **Configuration Groups**: Save and load different backup configurations (e.g., "Daily Work", "Full Drive Backup").
-   **Flexible Syncing**: Choose source and destination directories.
-   **Exclusion Rules**: Specify directories and files to ignore during backup (e.g., `node_modules`, `.tmp` files).
-   **Update Control**: Option to only update files that are newer in the source directory.
-   **Simple UI**: Easy-to-use graphical interface built with Tkinter.

## Technologies Used

-   Python 3
-   Tkinter (for the GUI)

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vavargasdev/va_pybackup.git
    cd va_pybackup
    ```

2.  **Run the application:**
    ```bash
    python main.py
    ```

3.  **Configuration:**
    -   The application uses a `backup_config.json` file to store backup groups.
    -   Fill in the fields in the UI to create a new configuration group.
    -   Enter a name for the group and click "Save Configuration".
    -   To run a backup, select a group from the dropdown and click "Start Backup".

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
