import beam
import nexus

class CreditTrader:
    def __init__(self, service_clients, a_quantity, a_security, b_security):
        self.state = None
        self.a_quantity = a_quantity
        self.a_security = a_security
        self.b_security = b_security
        self.a_order = None
        self.b_order = None
        self.a_latest_bbo_ask_price = None
        self.a_latest_bbo_bid_price = None
        self.b_latest_bbo_bid_price = None
        self.a_side = None
        self.b_side = None
        self.a_quantity_not_balanced = None
        self.a_quantity_filled = None
        self.b_latest_bbo_ask_price = None
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
            return self.S3()

    def S3(self):
        self.state = 3
        if self.C4():
            return self.S4()

    def S4(self):
        self.state = 4

    def S5(self):
        self.state = 5
        if self.C0():
            return self.S6()
        if self.C1():
            return self.S8()

    def S6(self):
        self.state = 6

    def S7(self):
        self.state = 7

    def S8(self):
        self.state = 8

    def S9(self):
        self.state = 9
        if self.C2():
            return self.S2()
        if not self.C2() and self.C3():
            return self.S5()
        if not self.C2() and not self.C3():
            return self.S10()

    def S10(self):
        self.state = 10

    def C0(self):

    def C1(self):

    def C2(self):

    def C3(self):

    def C4(self):

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
        if self.state == 5:
            return self.S5()
        if self.state == 6:
            return self.S7()
        if self.state == 8:
            return self.S9()

    def E6(self):
        if self.state == 5:
            return self.S5()

    def E7(self):
        if self.state == 6:
            return self.S7()

