import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

print(proxy.add(3,5))
