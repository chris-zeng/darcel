import beam
import nexus
class CreditTrader:
    def __init__(self):
        self.state==None
        
    def S9(self):
        if self.C2():
            return self.S2()
        if not self.C2() and self.C3():
            return self.S5()
        if not self.C2() and not self.C3():
            return self.S10()
    
    def S8(self):
    
    def S3(self):
        if self.C4():
            return self.S4()
    
    def S2(self):
        return self.S3()
    
    def S1(self):
    
    def S0(self):
    
    def S7(self):
    
    def S6(self):
    
    def S5(self):
        if self.C0():
            return self.S6()
        if self.C1():
            return self.S8()
    
    def S4(self):
    
    def S10(self):
    
    ###Conditions###
    def C3(self):
    
    def C2(self):
    
    def C1(self):
    
    def C0(self):
    
    def C4(self):
    
    ###Events###
    def E5(self):
        if self.state == 5:
            return self.S5()
        if self.state == 6:
            return self.S7()
        if self.state == 8:
            return self.S9()
    
    def E4(self):
        if self.state == 10:
            return self.S2()
    
    def E7(self):
        if self.state == 6:
            return self.S7()
    
    def E6(self):
        if self.state == 5:
            return self.S5()
    
    def E1(self):
        if self.state == 1:
            return self.S2()
    
    def E0(self):
        if self.state == 0:
            return self.S1()
        if self.state == 5:
            return self.S5()
    
    def E3(self):
        if self.state == 3:
            return self.S5()
        if self.state == 7:
            return self.S5()
    
    def E2(self):
        if self.state == 3:
            return self.S4()
        if self.state == 7:
            return self.S4()
        if self.state == 8:
            return self.S4()
    
