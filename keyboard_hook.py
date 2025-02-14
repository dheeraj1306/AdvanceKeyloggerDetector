import sys

def detect_keyboard_hook():
    if sys.platform == "win32":
        import ctypes
        try:
            wh_keyboard_ll = 13
            hooked = ctypes.windll.user32.CallNextHookEx(None, 0, 0, 0)
            if hooked:
                return ["Warning: A keyboard hook is detected! Possible keylogger."]
        except Exception:
            return []
    else:
        # Linux does not use `windll`, alternative method needed
        return check_linux_hooks()

    return []

def check_linux_hooks():
    detected = []
    
    # Check for known keylogger processes
    with open("/proc/modules", "r") as f:
        modules = f.read()
        if "evdev" in modules:  # `evdev` can be used for keylogging on Linux
            detected.append("Warning: evdev module detected. Possible keylogger.")

    # Check for suspicious processes
    try:
        import psutil
        suspicious_keywords = ["logkeys", "uberkey", "xinput", "interception"]
        for process in psutil.process_iter(attrs=['name']):
            if any(keyword in process.info['name'].lower() for keyword in suspicious_keywords):
                detected.append(f"Suspicious process detected: {process.info['name']}")
    except ImportError:
        detected.append("Warning: psutil not installed, cannot check processes.")
    
    return detected
