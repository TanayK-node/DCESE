class Process:
    def __init__ (self, pid, processes):
        self.pid = pid
        self.clock = [0] * processes
    def internal_event (self):
        self.clock[self.pid]+=1
        print (f"P[{self.pid}]: Internal event so clock is {self.clock} ")
    def send_message (self):
        self.clock[self.pid]+=1
        print (f"P[{self.pid}]: Sent message so clock is {self.clock} ")
        return list(self.clock)
    def receive_message (self, received_vector):
        for i in range (len (received_vector)):
            self.clock[i] = max (self.clock[i], received_vector[i])
        self.clock[self.pid] += 1
        print (f"P[{self.pid}]: Received message so clock is {self.clock} ")
    
p0 = Process (0, 3)
p1 = Process (1, 3)
p2 = Process (2, 3)

p0.internal_event()
msg = p0.send_message()
p1.receive_message(msg)
p2.internal_event()