from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn

class ThreadedXMLRPCServer(ThreadingMixIn,SimpleXMLRPCServer):pass

def add(a,b):
    return a+b

server=ThreadedXMLRPCServer(("localhost",8000))
server.register_function(add,"add")

server.serve_forever()
