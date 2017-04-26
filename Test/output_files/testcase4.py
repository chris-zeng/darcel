import beam
import nexus

class TestCase4:
    def __init__(self, service_clients, param4, param3, param2, param1):
        self.state = None
        self.param4 = param4
        self.param3 = param3
        self.param2 = param2
        self.param1 = param1
        self.var4 = None
        self.var1 = None
        self.var3 = None
        self.var2 = None
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

    def E0(self):
        if self.state == 0:
            return self.S1()

