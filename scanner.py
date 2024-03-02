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




def scan_port(ip: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    result = sock.connect_ex((ip, port))
    if DEBUG:
        print("[INFO] Scanning " + ip + ":" + str(port))
    if result == 0:
        return sock
    else:
        return False
            


def scan_ip(ip: str) -> list[tuple[str, int]]:
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



def is_bogon_ip(ip):
    bogon_ranges = [
        ipaddress.IPv4Network('0.0.0.0/8'),
        ipaddress.IPv4Network('10.0.0.0/8'),
        ipaddress.IPv4Network('100.64.0.0/10'),
        ipaddress.IPv4Network('127.0.0.0/8'),
        ipaddress.IPv4Network('127.0.53.53'),
        ipaddress.IPv4Network('169.254.0.0/16'),
        ipaddress.IPv4Network('172.16.0.0/12'),
        ipaddress.IPv4Network('192.0.0.0/24'),
        ipaddress.IPv4Network('192.0.2.0/24'),
        ipaddress.IPv4Network('192.168.0.0/16'),
        ipaddress.IPv4Network('198.18.0.0/15'),
        ipaddress.IPv4Network('198.51.100.0/24'),
        ipaddress.IPv4Network('203.0.113.0/24'),
        ipaddress.IPv4Network('224.0.0.0/4'),
        ipaddress.IPv4Network('240.0.0.0/4'),
        ipaddress.IPv4Network('255.255.255.255'),
    ]

    try:
        ip_obj = ipaddress.ip_address(ip)
        for bogon_range in bogon_ranges:
            if ip_obj in bogon_range:
                return True
            else:
                return False
    except Exception:
        return True
