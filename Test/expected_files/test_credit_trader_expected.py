import beam
import nexus

class CreditTrader:
    def __init__(self, service_clients):
        self.service_clients = service_clients
        self.state = None
        self.tasks = beam.RoutineTaskQueue()
        self.completion_queue = beam.Queue()

    def start(self):
        self.tasks.push(self.S0)

    def wait(self):
        self.completion_queue.top()
        
    def S0(self):
        self.state = 0
        
    def S1(self):
        self.state = 1
        
    def S2(self):
        self.state = 2
        return self.S3()
    
    def S3(self):
        self.state = 3
        
    def S4(self):
        self.state = 4
        
    def S5(self):
        self.state = 5
        
    def S6(self):
        self.state = 6
        
    def S7(self):
        self.state = 7
        
    def S8(self):
        self.state = 8
    
    def S9(self):
        self.state = 9
    
    def S10(self:)
        self.state = 10
        
    def C0(self):
    
    def C1(self):
    
    def C2(self):
    
    def C3(self):
    
    def E0(self):
        if self.state == 0:
            return self.S1()
        if self.state == 5:
            return self.S5()
    
    def E1(self):
        if self.state == 1:
            return self.S2()
            
    def E2(self):
        if self.state == 3:
            return self.S4()
        if self.state == 7:
            return self.S4()
        if self.state == 8:
            return self.S4()
    
    def E3(self):
        if self.state == 3:
            return self.S5()
        if self.state == 7:
            return self.S5()
            
    def E4(self):
        if self.state == 10:
            return self.S2()
                    
    def E5(self):
    
    def E6(self):