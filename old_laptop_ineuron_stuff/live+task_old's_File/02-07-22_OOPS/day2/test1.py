#from inside.insides import persons2
from inside import insides

obj1=insides.person2()
print(obj1.yob)
print(obj1._age(2003))
print((obj1._person2__age1(2009)))

class person1:
    def __init__(self , name ,surname , yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob

sudh = person1("sudhanshu" , "kumar" , 1990)
print(sudh._name1)
print(sudh._person1__surname1)
