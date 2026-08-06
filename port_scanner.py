import socket
import threading 

target = "127.0.0.1"
start_port = 1
end_port = 9000

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8000: "HTTP (alt)",
    9000: "HTTP (alt)"
}

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port))
    if result == 0:
        service = common_ports.get(port, "Unknown")
        print(f"Port {port} is open - {service}")
    s.close()

threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(target, port))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Scanning completed.")