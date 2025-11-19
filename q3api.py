import time, uuid, threading

KEY_TTL = 10        # seconds (use 300 in real assignment)
BLOCK_TIMEOUT = 5   # seconds (use 60 in real assignment)

keys = {}  # key -> [status, expires_at, blocked_at]
lock = threading.Lock()

def cleaner():
    while True:
        time.sleep(1)
        with lock:
            now = time.time()
            for k, v in list(keys.items()):
                if v[1] < now: keys.pop(k); continue
                if v[0]=="blocked" and now - v[2] > BLOCK_TIMEOUT:
                    v[0]="available"; v[2]=None

threading.Thread(target=cleaner, daemon=True).start()

def create_key():
    k = uuid.uuid4().hex[:6]
    with lock: keys[k] = ["available", time.time()+KEY_TTL, None]
    return k

def get_key():
    with lock:
        for k, v in keys.items():
            if v[0]=="available":
                v[0]="blocked"; v[2]=time.time()
                return k
    return None

def keep_alive(k):
    with lock:
        if k in keys: keys[k][1] = time.time()+KEY_TTL

# ------- Demo -------
if __name__=="__main__":
    k1 = create_key(); print("Created:", k1)
    time.sleep(1)
    g = get_key(); print("Got:", g)
    time.sleep(6)  # auto-unblock
    print("After unblock:", get_key())
    keep_alive(k1)
    print("Keep-alive done for", k1)
    time.sleep(12)
    print("Final keys:", keys)
