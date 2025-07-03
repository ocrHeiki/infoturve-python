import socket

domeen = input("Sisesta domeen (näiteks: google.com): ")
try:
    ip = socket.gethostbyname(domeen)
    print(f"{domeen} IP-aadress on {ip}")
except socket.gaierror:
    print("Viga: domeeni ei leitud.")
