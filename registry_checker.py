import winreg

def check_registry():
    suspicious_keys = [
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run")
    ]

    detected = []
    for hkey, subkey in suspicious_keys:
        try:
            with winreg.OpenKey(hkey, subkey, 0, winreg.KEY_READ) as reg_key:
                i = 0
                while True:
                    try:
                        value = winreg.EnumValue(reg_key, i)
                        if "keylogger" in value[1].lower():
                            detected.append(f"Suspicious registry key found: {value[0]} - {value[1]}")
                        i += 1
                    except OSError:
                        break
        except FileNotFoundError:
            pass

    return detected

def remove_registry_entries():
    suspicious_keys = [
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run")
    ]

    for hkey, subkey in suspicious_keys:
        try:
            with winreg.OpenKey(hkey, subkey, 0, winreg.KEY_SET_VALUE) as reg_key:
                winreg.DeleteValue(reg_key, "keylogger")
                print("Removed suspicious registry key")
        except FileNotFoundError:
            pass
