import time, random, threading

class Server:
    def __init__(self, sid): self.sid, self.lc = sid, 0
    def event(self):
        self.lc += 1
        raw = time.time() + random.uniform(-2, 2)   # unsynced clock
        return {"server": self.sid, "raw": raw, "lamport": self.lc,
                "msg": f"Event from S{self.sid}"}

class Manager:
    def __init__(self): self.logs = []
    def collect(self, log): self.logs.append(log)
    def show(self):
        for l in sorted(self.logs, key=lambda x: x["lamport"]):
            print(f"L={l['lamport']} | RAW={l['raw']:.2f} | S{l['server']} | {l['msg']}")

servers = [Server(i) for i in range(1,4)]
mgr = Manager()

def run_server(s):
    for _ in range(3):
        time.sleep(random.uniform(0.1,0.5))
        mgr.collect(s.event())

threads = [threading.Thread(target=run_server, args=(s,)) for s in servers]
[t.start() for t in threads]
[t.join() for t in threads]

print("\n--- Centralized Ordered Logs (Lamport Ordered) ---")
mgr.show()
