from mcstatus import JavaServer
import socket

DEBUG = False

def scan_port(sock: socket.socket, ip: str, port: int) -> bool:
    result = sock.connect_ex((ip, port))
    if DEBUG:
        print("[INFO] Scanning " + ip + ":" + str(port))
    return bool(result == 0)


def scan_ip(sock: socket.socket, ip: str, ports: list[int]) -> list[tuple[str, int]]:
    open_ports = []
    for port in ports:
      if scan_port(sock=sock, ip=ip, port=port):
        open_ports.append((ip, port))
    return open_ports

def is_mcserver(ip):
    server = JavaServer.lookup(ip)
    try:
        status = server.status()
        return True
    except Exception:
        return False