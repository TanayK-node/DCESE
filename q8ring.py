class Node:
    def __init__(self, id):
        self.id = id
        self.active = True

def ring_election(nodes, initiator_index):
    n = len(nodes)
    msg = []
    curr = initiator_index
    print(f"--- Election Started by Node {nodes[curr].id} ---")
    while True:
        if nodes[curr].active:
            msg.append(nodes[curr].id)
            print(f" -> Passed to Node {nodes[curr].id}, list is now: {msg}")
        else:
            print(f" XX Node {nodes[curr].id} is DEAD. Skipping.")
        curr = (curr + 1) % n
        if curr == initiator_index:
            break
    coordinator = max(msg)
    print(f"\nElection message passed: {msg}")
    print(f"New coordinator is Node {coordinator}")

nodes = [Node(i) for i in range(1, 6)]
print("Crash! Node 5 fails.") 
nodes[4].active = False 
ring_election(nodes, initiator_index=2)