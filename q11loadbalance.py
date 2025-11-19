import time

class BackendServer:
    def __init__(self, name):
        self.name = name

    def handle_request(self, req_id):
        print(f"   [Server {self.name}] Processing Request #{req_id}...")

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0  # Pointer to the current server

    def forward_request(self, req_id):
        # 1. Select server using Round Robin Logic
        selected_server = self.servers[self.current_index]
        
        print(f"[Load Balancer] Routing Request #{req_id} to -> {selected_server.name}")
        selected_server.handle_request(req_id)

        # 2. Update pointer (Circular increment)
        self.current_index = (self.current_index + 1) % len(self.servers)

# --- SIMULATION ---

# 1. Setup 3 Backend Servers
backends = [BackendServer("A"), BackendServer("B"), BackendServer("C")]

# 2. Initialize Load Balancer
lb = LoadBalancer(backends)

print("--- STARTING TRAFFIC SIMULATION (Round Robin) ---")

# 3. Simulate 7 User Requests
for i in range(1, 8):
    lb.forward_request(i)
    time.sleep(0.5) # Short delay to make output readable