import socket
import threading
import argparse
import queue

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
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            service = common_ports.get(port, "Unknown")
            print(f"Port {port} is open - {service}")
        s.close()
    except socket.error:
        pass

def worker(target, q):
    while not q.empty():
        port = q.get()
        scan_port(target, port)
        q.task_done()

parser = argparse.ArgumentParser()
parser.add_argument("target", help="Target IP address or hostname")
parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
parser.add_argument("--end", type=int, default=9000, help="End port (default: 9000)")
parser.add_argument("--threads", type=int, default=100, help="Number of threads (default: 100)")
args = parser.parse_args()

threads = []

port_queue = queue.Queue()
for port in range(args.start, args.end + 1):
    port_queue.put(port)

for _ in range(args.threads):
    t = threading.Thread(target=worker, args=(args.target, port_queue))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Scanning completed.")