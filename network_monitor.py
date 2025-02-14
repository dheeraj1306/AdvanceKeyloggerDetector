import psutil

def detect_network_activity():
    detected = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'ESTABLISHED':
            detected.append(f"Active Connection: {conn.laddr} -> {conn.raddr}")
    return detected
