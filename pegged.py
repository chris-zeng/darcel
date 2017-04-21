import beam
import nexus
class PeggedOrder:
    def __init__():
    ###States###
    def S0(self):
    
    def S1(self):
    
    def S2(self):
    
    def S3(self):
        if self.C0():
            return self.S5()
    
    def S4(self):
    
    def S5(self):
    
    ###Conditions###
    def C0(self):
    
    ###Events###
    def E0(self):
        if self.state == 0:
            return self.S1()
        if self.state == 3:
            return self.S3()
    
    def E1(self):
        if self.state == 1:
            return self.S2()
    
    def E2(self):
        if self.state == 1:
            return self.S3()
    
    def E3(self):
        if self.state == 3:
            return self.S4()
        if self.state == 5:
            return self.S4()
    
    def E4(self):
        if self.state == 5:
            return self.S1()
    
