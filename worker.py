import random
import socket
import scanner
import time

PORTS_TO_SCAN = []
TIMEOUT = 1

running = True


GREEN = "\033[1;32;48m"
YELLOW = "\033[1;33;48m"
RED = "\033[1;31;48m"
END = "\033[1;37;0m"


def config(ports, timeout):
    global PORTS_TO_SCAN, TIMEOUT
    PORTS_TO_SCAN = ports
    TIMEOUT = timeout


def stop_threads():
    global running
    running = False


def random_ip() -> str:
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"


def log_server(ip, port):
    try:
        with open("found_servers.txt", "a") as file:
           file.write(ip + ":" + str(port) + "\n")
           print("[INFO] " + GREEN + "Successfully wrote the server " + ip + ":" + str(port) + " to the server list" + END)
    except Exception:
       print(RED + "[WARN] An error occured while writing to the server list" + END)



def run_worker():
    time.sleep(1)

    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        scan_ip = random_ip()
        results = scanner.scan_ip(sock=sock, ip=scan_ip, ports=PORTS_TO_SCAN)
        if results:
            for result in results:
                ip, port = result[0], result[1]
                print("[INFO] " + YELLOW + "Found ip: " + ip + ":" + str(port) + ", checking for minecraft servers..." + END)
                if scanner.is_mcserver(ip + ":" + str(port)):
                    print("[INFO] " + GREEN + "[SERVER] Found server: " + ip + ":" + str(port) + END)
                    log_server(ip=ip, port=port)
                else:
                    print("[INFO] " + YELLOW + "Did not find any server on: " + ip + ":" + str(port) + END)
        sock.close()
        if not running:
            break
