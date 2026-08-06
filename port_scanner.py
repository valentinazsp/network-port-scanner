import socket
import threading 

target = "127.0.0.1"
start_port = 1
end_port = 9000

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()

threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(target, port))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Scanning completed.")