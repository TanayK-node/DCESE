class Node:
    def __init__(self, id):
        self.id = id
        self.alive = True

    def start_election(self, all_nodes):
        print(f"\n[Node {self.id}] starts ELECTION. Checking higher priority nodes...")
        higher_nodes = [n for n in all_nodes if n.id > self.id]
        found_higher = False
        for node in higher_nodes:
            print(f"  -> [Node {self.id}] sends ELECTION to [Node {node.id}]")
            if node.alive:
                print(f"  <- [Node {node.id}] responds OK. [Node {self.id}] stops.")
                found_higher = True
                node.start_election(all_nodes)
                break
            else:
                print(f"  XX [Node {node.id}] is DEAD. No response.")
        if not found_higher:
            self.become_coordinator(all_nodes)

    def become_coordinator(self, all_nodes):
        print(f"\n[Node {self.id}] wins! I am the new COORDINATOR.")
        print(f"[Node {self.id}] broadcasting COORDINATOR message to all.")
        for n in all_nodes:
            if n.alive and n.id != self.id:
                print(f"  -> [Node {self.id}] alerts [Node {n.id}]: New Leader is {self.id}")

nodes = [Node(i) for i in range(5)]
print(f"---System Started. Current Leader: Node 4 ---")
print("\n---CRASH: Node 4 fails ---")
nodes[4].alive = False
nodes[1].start_election(nodes)