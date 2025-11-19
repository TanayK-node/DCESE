import time

class Replica:
    def __init__(self, id):
        self.id = id
        self.data = {} 

    def write(self, key, value):
        self.data[key] = value
        print(f"[{self.id}] WRITE: Set {key} = {value}")

    def read(self, key):
        value = self.data.get(key, "None")  
        print(f"[{self.id}] READ : {key} = {value}")

    def propagate_from(self, master_node):
        print(f"   ... [System] Propagating data from {master_node.id} to {self.id} ...")
        self.data = master_node.data.copy()

nodes = [Replica("Node_A"), Replica("Node_B"), Replica("Node_C")]

print("--- STEP 1: User updates Node_A (Primary) ---")
nodes[0].write("price", 500)

print("\n--- STEP 2: Immediate Read (The 'Inconsistent' Window) ---")
nodes[0].read("price")
nodes[1].read("price")
nodes[2].read("price")
print(">> RESULT: Nodes are INCONSISTENT (Different values returned)")

print("\n--- STEP 3: Simulate Network Delay & Propagation ---")
time.sleep(2) 
nodes[1].propagate_from(nodes[0])
nodes[2].propagate_from(nodes[0])

print("\n--- STEP 4: Read After Delay (Eventual Consistency) ---")
nodes[0].read("price")
nodes[1].read("price")
nodes[2].read("price")
print(">> RESULT: Nodes are CONSISTENT (All match)")