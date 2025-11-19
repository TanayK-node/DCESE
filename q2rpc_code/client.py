import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Send tasks to server
print("Add:", server.execute_task("add", 10, 5))
print("Multiply:", server.execute_task("multiply", 7, 6))
print("Reverse:", server.execute_task("reverse", "hello"))
print("Sort:", server.execute_task("sort", [5, 2, 9, 1]))
