import socket 

with socket.socket() as s :
    s.connect(("localhost",8000))
    while True:
        msg=input("You : ")
        if not msg :
            break
        s.send(msg.encode())
        print(f"Server : {s.recv(1024).decode()}")