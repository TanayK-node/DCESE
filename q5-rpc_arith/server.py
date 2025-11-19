from xmlrpc.server import SimpleXMLRPCServer

# Arithmetic functions to expose
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Arithmetic RPC Server running on port 8000...")

# Register functions for remote access
server.register_function(add, "add")
server.register_function(sub, "sub")
server.register_function(mul, "mul")

# Keep server running
server.serve_forever()
