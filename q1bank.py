class Server:
    def __init__(self, id):
        self.id = id
        self.alive = True
        self.balance = 1000

    def elect(self, all_nodes):
        # Check every node to see if there is a bigger one
        for node in all_nodes:
            if node.id > self.id and node.alive:
                # If a higher node is found, let them run the election
                return node.elect(all_nodes)
        
        # If loop finishes and no higher node was found, I am the winner
        return self

# --- SIMULATION ---
servers = [Server(1), Server(2), Server(3)]

print("--- Crash Node 3 ---")
servers[2].alive = False 

# 1. Election: Node 1 notices crash and starts election
leader = servers[0].elect(servers)
print(f"New Leader is Node {leader.id}")

# 2. Sync & Transaction
for s in servers:
    if s.alive:
        s.clock = 100 # Sync time
        
leader.balance -= 100
print(f"Transaction Done. Balance: {leader.balance}")