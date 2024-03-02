from threading import Thread
import worker
import time
import json


VERSION = "v1.1.0"


with open("config.json", "r") as file:
    global CONFIG
    CONFIG = json.load(file)

WORKERS = CONFIG["WORKERS"]
PORTS = CONFIG["PORTS"]



print("[INFO] Starting Copenheimer " + VERSION + " with " + str(WORKERS) + " workers")
print("[INFO] Starting workers...")


workers_list: list[Thread] = []

for i in range(WORKERS):
    new_worker = Thread(target=worker.run_worker)
    workers_list.append(new_worker)
    new_worker.start()

print("[INFO] Started " + str(WORKERS) + " workers")


print("[INFO] Scaning on ports: ", end="")
for port in PORTS[:-1]:
    print(port, end=", ")
print(PORTS[-1])

print("[INFO] Scanning for servers...")
print("[INFO] Press control + c to exit")



try:
    while True: 
        time.sleep(1)

except KeyboardInterrupt:
    print()
    print("[INFO] Shutting down Copenheimer...")
    print("[INFO] Stopping workers...")

    worker.stop_threads()
    for worker_to_stop in workers_list:
        while worker_to_stop.is_alive():
            time.sleep(0.1)

    print("[INFO] Copenheimer has been shut down")
