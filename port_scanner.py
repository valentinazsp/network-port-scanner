import socket
target = "127.0.0.1"
start_port = 1
end_port = 1024

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is open")
        s.close()

print("Scanning completed.")