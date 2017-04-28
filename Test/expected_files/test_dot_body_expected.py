import beam
import nexus

class test_dot_body:
    def __init__(self, service_clients, param1, param2, param3):
        self.state = None
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.var1 = None
        self.var2 = None
        self.var3 = None
        self.service_clients = service_clients
        self.tasks = beam.RoutineTaskQueue()
        self.completion_queue = beam.Queue()
        self.market_data_client = self.\
                service_clients.get_market_data_client()
        self.order_execution_client = self.service_clients.\ 
                get_order_execution_client()

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

    def S3(self):
        self.state = 3
        return self.S4()

    def S4(self):
        self.state = 4

    def E0(self):
        if self.state == 0:
            return self.S1()

    def E1(self):
        if self.state == 1:
            return self.S2()

    def E2(self):
        if self.state == 2:
            return self.S3()

