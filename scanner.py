import socket
import json
import statusping
import ipaddress

with open("config.json", "r") as file:
    global CONFIG
    CONFIG = json.load(file)

TIMEOUT = CONFIG["TIMEOUT"]
PORTS = CONFIG["PORTS"]
DEBUG = CONFIG["DEBUG"]


# Ips that you should proably not scan if you don't want legal trouble
BAD_IPS = []
with open("exclude.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        line = line.split(" ")[0]
        line
        if len(line) == 0:
            continue
        if line[0] == "#":
            continue
        if "-" in line:
            start_ip, end_ip = line.split('-')
            start_ip, end_ip = ipaddress.IPv4Address(start_ip.strip()), ipaddress.IPv4Address(end_ip.strip())
            BAD_IPS.extend(list(ipaddress.summarize_address_range(start_ip, end_ip)))
        else:
            BAD_IPS.append(ipaddress.IPv4Network(line))



def scan_port(ip: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    result = sock.connect_ex((ip, port))
    if DEBUG:
        print("[INFO] Scanning " + ip + ":" + str(port))
    if result == 0:
        return sock
    else:
        return False
            


def scan_ip(ip: str):
    open_ports = []
    for port in PORTS:
        res = scan_port(ip=ip, port=port)
        if type(res) == socket.socket:
            open_ports.append((ip, port, res))
    return open_ports


def is_mcserver(ip, port, sock):
    sp = statusping.StatusPing(ip, port)
    try:
        res = sp.get_status(sock)
        return res
    except Exception:
        return False



def is_bad_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        for range in BAD_IPS:
            if ip_obj in range:
                return True
            else:
                return False
    except Exception:
        return True
