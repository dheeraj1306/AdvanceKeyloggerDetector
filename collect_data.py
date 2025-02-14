import psutil
import pandas as pd

def collect_process_data():
    data = []
    
    for process in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']):
        process_name = process.info['name'].lower()
        
        # Manually label keylogger-like processes (1 = Malicious, 0 = Normal)
        suspicious_keywords = ["keylog", "logger", "stealer", "spy", "hook", "keyboard"]
        label = 1 if any(keyword in process_name for keyword in suspicious_keywords) else 0
        
        data.append([process.info['name'], process.info['cpu_percent'], process.info['memory_percent'], label])
    
    return data

# Collect process data and save to CSV
process_data = collect_process_data()
df = pd.DataFrame(process_data, columns=['Process_Name', 'CPU_Usage', 'Memory_Usage', 'Label'])
df.to_csv("process_dataset.csv", index=False)

print("[INFO] Process data collected and saved to process_dataset.csv")
