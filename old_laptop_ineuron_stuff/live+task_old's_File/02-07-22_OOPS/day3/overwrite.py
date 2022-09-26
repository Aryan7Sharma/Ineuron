class ineuron:
    def __init__(self):
        self.student="Data science"
    def students(self):
        print("student of ineuron in ",self.student)
i=ineuron()
i.students()
print(i.student)
i.student="data analytics" # overwriting the class variable on a run time
i.students()
print(i.student)

# we can not modify any class variable directly if it there is a method for that like getter and setter

class ineuron1:
    def __init__(self):
        self.__student="Dataa science"
    def students(self):
        print("student of ineuron1 in ",self.__student)

    def change_value(self,newval):
        self.__student=newval

i1=ineuron1()
i1.students()
print(i1._ineuron1__student)
i1.__student="data analytics"
i1.students()
print(i1.__student)
i1.students()
i1.change_value("now its changed!!")
i1.students()