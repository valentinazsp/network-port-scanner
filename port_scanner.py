import socket
import threading
import argparse

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

parser = argparse.ArgumentParser()
parser.add_argument("target", help="Target IP address or hostname")
parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
parser.add_argument("--end", type=int, default=9000, help="End port (default: 9000)")
args = parser.parse_args()

threads = []

for port in range(args.start, args.end + 1):
    t = threading.Thread(target=scan_port, args=(args.target, port))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Scanning completed.")