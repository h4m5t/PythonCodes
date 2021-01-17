import socket


for port in range(440, 445):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) 
    state = sock.connect_ex(("3.80.150.152", port))
    if 0 == state:
        print("port: {} is open".format(port))
    sock.close()