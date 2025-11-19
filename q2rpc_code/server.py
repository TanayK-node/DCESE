from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading

# --- Threaded Server Wrapper ---
class ThreadedXMLRPCServer(SimpleXMLRPCServer):
    def process_request_thread(self, request, client_address):
        """Handle each request in a new thread."""
        try:
            self.finish_request(request, client_address)
            self.shutdown_request(request)
        except Exception:
            self.handle_error(request, client_address)
            self.shutdown_request(request)

    def process_request(self, request, client_address):
        t = threading.Thread(
            target=self.process_request_thread,
            args=(request, client_address)
        )
        t.daemon = True
        t.start()

# --- Remote Execution Logic ---
def execute_task(task_name, *args):
    """A tiny sandbox of allowed functions."""
    
    allowed_tasks = {
        "add": lambda a, b: a + b,
        "multiply": lambda a, b: a * b,
        "reverse": lambda s: s[::-1],
        "sort": lambda arr: sorted(arr),
    }

    if task_name not in allowed_tasks:
        return f"Error: Task '{task_name}' not allowed."

    return allowed_tasks[task_name](*args)

# --- Start Server ---
if __name__ == "__main__":
    print("Remote Execution Server running on port 8000...")
    server = ThreadedXMLRPCServer(("0.0.0.0", 8000), allow_none=True)
    server.register_function(execute_task, "execute_task")
    server.serve_forever()
