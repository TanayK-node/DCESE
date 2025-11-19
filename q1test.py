import random, time

class Server:
    def __init__(self, sid): self.id, self.lc, self.alive = sid, 0, True
    def tick(self): self.lc += 1; return self.lc
    def crash(self): self.alive = False
    def revive(self): self.alive = True

def bully_elect(servers):
    alive = [s for s in servers if s.alive]
    return max(alive, key=lambda s: s.id)

def transaction(server, amount, bal):
    if not server.alive: return bal
    ts = server.tick()   # Lamport logical timestamp
    return bal + amount, ts

# --- Simulation ----
servers = [Server(i) for i in range(1,5)]
leader = bully_elect(servers)
balance, history = 100, []

print("Initial Leader:", leader.id)

# Some transactions
for s in servers:
    balance, ts = transaction(s, +10, balance)
    history.append((ts, f"S{s.id} +10"))

# Leader crashes
leader.crash()
print("Leader Crashed:", leader.id)

# Re-elect new leader
leader = bully_elect(servers)
print("New Leader:", leader.id)

# New transactions after crash
for s in servers:
    if s.alive:
        balance, ts = transaction(s, -5, balance)
        history.append((ts, f"S{s.id} -5"))

# Global ordering done by Lamport timestamps
print("\n--- Global Ordered Log ---")
for ts, log in sorted(history): print(ts, log)
print("\nFinal Balance:", balance)
