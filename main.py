from threading import Thread
import worker
import time
import json


VERSION = "v1.3.0"


with open("config.json", "r") as file:
    global CONFIG
    CONFIG = json.load(file)

WORKERS = CONFIG["WORKERS"]
BATCH_SIZE = CONFIG["BATCH_SIZE"]
PORTS = CONFIG["PORTS"]
TIMEOUT = CONFIG["TIMEOUT"]
DEBUG = CONFIG["DEBUG"]
USE_WEBHOOK = CONFIG["USE_WEBHOOK"]

RATE = ((WORKERS * BATCH_SIZE) / len(PORTS)) / TIMEOUT




print(f"""

      



     _____ ____  _____  ______ _   _ _    _ ______ _____ __  __ ______ _____  
    / ____/ __ \|  __ \|  ____| \ | | |  | |  ____|_   _|  \/  |  ____|  __ \ 
   | |   | |  | | |__) | |__  |  \| | |__| | |__    | | | \  / | |__  | |__) |
   | |   | |  | |  ___/|  __| | . ` |  __  |  __|   | | | |\/| |  __| |  _  / 
   | |___| |__| | |    | |____| |\  | |  | | |____ _| |_| |  | | |____| | \ \ 
    \_____\____/|_|    |______|_| \_|_|  |_|______|_____|_|  |_|______|_|  \_\\



Copenheimer {VERSION}
https://github.com/JacobborstellCoder/Horrible_copenheimer
                                                   
""")





print("[INFO] Starting Copenheimer " + VERSION + " with " + str(WORKERS) + " workers and a batch size of " + str(BATCH_SIZE))

if DEBUG:
    print("[INFO] Debug is enabled")

if USE_WEBHOOK:
    print("[INFO] Discord webhooks is enabled")

print("[INFO] Scaning on ports: ", end="")
for port in PORTS[:-1]:
    print(port, end=", ")
print(PORTS[-1], "with a timeout of " + str(TIMEOUT) + " seconds")

print("[INFO] Estimated rate: " + str(RATE) + " IP's per second")
print()
print("[INFO] Starting " + str(WORKERS) +  " workers...", end=" ")


workers_list = []

for i in range(WORKERS):
    new_worker = Thread(target=worker.run_worker)
    workers_list.append(new_worker)
    new_worker.start()

print("done")
print("[INFO] Scanning for servers, press control + c to exit")
print()



try:
    while True: 
        time.sleep(1)

except KeyboardInterrupt:
    print()
    print("[INFO] Shutting down Copenheimer...")
    print("[INFO] Stopping workers... ")

    worker.stop_threads()
    for worker_to_stop in workers_list:
        while worker_to_stop.is_alive():
            time.sleep(0.1)

    print("[INFO] Copenheimer has been shut down")
