import socket
import threading

# Handle each client in its own thread
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print(f"[{addr}] sent:", data)

        # Simple processing: convert text to uppercase
        response = data.upper()

        conn.send(response.encode())

    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 8000))
    server.listen()

    print("🟢 Server running on port 8000...")
    print("Waiting for clients...\n")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE THREADS] {threading.active_count() - 1}")  # minus main thread


if __name__ == "__main__":
    start_server()
