from socketserver import ThreadingMixIn
from socketserver import BaseRequestHandler
from socketserver import TCPServer


class Handler(BaseRequestHandler):
    def handle(self):
        addr =self.client_address
        print(f"[NEW ] {addr} Conneted" )
        while(data := self.request.recv(1024)):
            print(f" {addr} : {data}")
            self.request.sendall(data)
        print(f"[LEFT] {addr} Disconected")
    

class Server(ThreadingMixIn,TCPServer):pass

if __name__=="__main__":
    with Server(("localhost",8000),Handler) as s:
        print(f"Connected on port 8000..")
        s.serve_forever()

