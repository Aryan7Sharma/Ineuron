class Car:
    def __init__(self,body,en,t):
        self.body=body
        self.engine=en
        self.tyre=t

    def milage(self):
        print("milage of this car")

c=Car("sold","v97","radical")
print(c.engine)