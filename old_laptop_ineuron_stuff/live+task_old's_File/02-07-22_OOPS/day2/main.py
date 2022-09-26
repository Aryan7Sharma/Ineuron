class Enrolled:
    def __init__(self,*args):
        self.count=0
        for i,j in enumerate(args):
            self.i=j
            self.count+=1
    def p(self):
        for i in range(self.count):
            print(self.i)

obj=Enrolled("Fsda","fsds","fds")
obj.p()
