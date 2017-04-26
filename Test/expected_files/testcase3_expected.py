import beam
import nexus

class TestCase3:
    def __init__(self, service_clients):
        self.state = None
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
        if self.C0():
            return self.S5()

    def S1(self):
        self.state = 1

    def S2(self):
        self.state = 2

    def S4(self):
        self.state = 4

    def S5(self):
        self.state = 5

    def C0(self):

    def E0(self):
        if self.state == 0:
            return self.S1()

    def E1(self):
        if self.state == 0:
            return self.S2()

    def E3(self):
        if self.state == 0:
            return self.S4()

