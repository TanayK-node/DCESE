import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8000))

print("Connected to server. Type messages (type 'exit' to quit)")

while True:
    msg = input("> ")
    if msg.lower() == "exit":
        break

    client.send(msg.encode())
    response = client.recv(1024).decode()
    print("Server:", response)

client.close()
