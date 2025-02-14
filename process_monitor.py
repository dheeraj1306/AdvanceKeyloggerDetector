import psutil
from ml_analyzer import analyze_process

def detect_suspicious_processes():
    detected = []
    
    for process in psutil.process_iter(attrs=['pid', 'name']):
        process_data=[process.cpu_percent(interval=0),process.memory_percent()]
        try:
            cpu_usage = process.info.get('cpu_percent', 0)  # Default to 0 if missing
            memory_usage = process.info.get('memory_percent', 0)  # Default to 0 if missing
            process_data = [cpu_usage, memory_usage]
            
            if analyze_process(process_data):
                detected.append(f"Suspicious Process: {process.info['name']} (PID: {process.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  # Skip processes that no longer exist or cannot be accessed

    return detected

def remove_suspicious_processes():
    for process in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            cpu_usage = process.info.get('cpu_percent', 0)
            memory_usage = process.info.get('memory_percent', 0)
            if analyze_process([cpu_usage, memory_usage]):
                psutil.Process(process.info['pid']).terminate()
                print(f"Terminated process: {process.info['name']} (PID: {process.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  # Skip inaccessible or non-existent processes
