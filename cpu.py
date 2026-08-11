class CPU:
    def __init__(self):
        self.accumulator = 0

    def load(self, value):
        self.accumulator = value
    def add(self,value):
        self.accumulator+=value    
    def sub(self,value):
        self.accumulator-=value
    def mul(self,value):
        self.accumulator*=value
    def div(self,value):
        self.accumulator/=value
    def print_acc(self):
        print(self.accumulator)                     