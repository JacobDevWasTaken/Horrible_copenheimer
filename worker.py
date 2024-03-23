import random
import time
import json
import asyncio
import ipaddress
import mcstatus



running = True



with open("config.json", "r") as file:
    global CONFIG
    CONFIG = json.load(file)

TIMEOUT = CONFIG["TIMEOUT"]
DEBUG = CONFIG["DEBUG"]
PORTS = CONFIG["PORTS"]
BATCH_SIZE = CONFIG["BATCH_SIZE"]
USE_WEBHOOK = CONFIG["USE_WEBHOOK"]



GREEN = "\033[1;32;48m"
YELLOW = "\033[1;33;48m"
RED = "\033[1;31;48m"
END = "\033[1;37;0m"


if USE_WEBHOOK:
    from discord_webhook import DiscordWebhook
    with open("webhook.txt") as file:
        WEBHOOK_URL = file.read().strip("\n")


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



def is_bad_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        for range in BAD_IPS:
            if ip_obj in range:
                return True
    
    except Exception:
        return True
    
    return False



def log_server(ip, port):
    try:
        with open("found_servers.txt", "a") as file:
           file.write(ip + ":" + str(port) + "\n")

    except Exception:
       print(RED + "[WARN] An error occured while writing to the server list" + END)

    finally:
        if USE_WEBHOOK:
            webhook = DiscordWebhook(url=WEBHOOK_URL, content="Found minecraft server: " + ip + ":" + str(port)).execute()


def stop_threads():
    global running
    running = False


def random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"







def is_mcserver(ip, port):
    try:
        obj = mcstatus.JavaServer(host=ip, port=port, timeout=TIMEOUT * 2)
        res = obj.status()
        return True
    except Exception as e:
        return False


async def scan_port(ip: str, port: int):
    if DEBUG:
        print("[INFO] Scanning:", ip + ":" + str(port))
    
    try:
        r, w = await asyncio.wait_for(asyncio.open_connection(host=ip, port=port), TIMEOUT)
        w.close()

        if is_mcserver(ip, port):
            print("[INFO] " + GREEN + "[SERVER] Found minecraft server: " + ip + ":" + str(port) + END)
            log_server(ip, port)

    except Exception:
        pass


async def scan_batch(size):
    tasks = []

    for i in range(round(size / len(PORTS))):
        scan_ip = random_ip()
        if is_bad_ip(scan_ip):
            continue

        for port in PORTS:
            tasks.append(scan_port(scan_ip, port))
        
    await asyncio.gather(*tasks)


def run_worker():
    time.sleep(1)

    while True:
        asyncio.run(scan_batch(BATCH_SIZE))

        if not running:
            break
