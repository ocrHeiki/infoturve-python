import socket

ip = input("Sisesta IP-aadress: ")
for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    tulemus = s.connect_ex((ip, port))
    if tulemus == 0:
        print(f"Port {port} on avatud.")
    s.close()
