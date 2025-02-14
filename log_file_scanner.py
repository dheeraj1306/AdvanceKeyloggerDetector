import os

log_paths = ["C:\\Users\\Public\\log.txt", "C:\\Windows\\System32\\keystrokes.log"]

def scan_log_files():
    detected = []
    for path in log_paths:
        if os.path.exists(path):
            detected.append(f"Possible keylogger log file found: {path}")
    return detected

def remove_log_files():
    for path in log_paths:
        if os.path.exists(path):
            try:
                os.remove(path)
                print(f"Deleted log file: {path}")
            except Exception as e:
                print(f"Failed to delete {path}: {e}")
