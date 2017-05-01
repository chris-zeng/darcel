import beam
import nexus

class test_conditions:
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
        if self.C0():
            return self.S1()

    def S1(self):
        self.state = 1
        if not self.C1():
            return self.S2()

    def S2(self):
        self.state = 2
        if self.C0() or self.C1():
            return self.S3()

    def S3(self):
        self.state = 3
        if self.C1() and self.C0():
            return self.S4()

    def S4(self):
        self.state = 4
        if self.C0() or self.C1() and self.C2():
            return self.S5()

    def S5(self):
        self.state = 5

    def C0(self):
        pass

    def C1(self):
        pass

    def C2(self):
        pass

