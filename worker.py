import random
import scanner
import time


GREEN = "\033[1;32;48m"
YELLOW = "\033[1;33;48m"
RED = "\033[1;31;48m"
END = "\033[1;37;0m"


running = True



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
        scan_ip = random_ip()
        if scanner.is_bogon_ip(scan_ip):
            continue
        results = scanner.scan_ip(scan_ip)
        if results:
            for result in results:
                ip, port, sock = result[0], result[1], result[2]
                print("[INFO] " + YELLOW + "Found ip with port open: " + ip + ":" + str(port) + ", checking for minecraft servers..." + END)
                res = scanner.is_mcserver(ip, port, sock)
                if res:
                    print("[INFO] " + GREEN + "[SERVER] Found minecraft server: " + ip + ":" + str(port) + END)
                    log_server(ip=ip, port=port)
                else:
                    print("[INFO] " + YELLOW + "Did not find any minecraft server on: " + ip + ":" + str(port) + END)
        if not running:
            break
