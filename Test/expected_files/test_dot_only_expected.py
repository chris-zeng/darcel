import beam
import nexus

class test_dot_only:
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

    def S3(self):
        self.state = 3

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

    def E3(self):
        if self.state == 3:
            return self.S4()

