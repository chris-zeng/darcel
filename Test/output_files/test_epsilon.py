import beam
import nexus

class test_epsilon:
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
        return self.S1()

    def S1(self):
        self.state = 1

