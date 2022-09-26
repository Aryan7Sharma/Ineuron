class Ineuron:
    def students(self):
        print("print a students details")

class class_type:
    def students(self):
        print("print the class type of students")

def Ineuron_external(a):
    a.students()

i=Ineuron()
j=class_type()
Ineuron_external(i)
Ineuron_external(j)




'''def test(a,b):
    return a+b
print(test(1,3)) # this time it perform addition
print(test("aryan","sharma")) # and for this it perform concatenation
'''
'''
One person Multiple behaviour means its do a different different work for different - different  data or in
 different - different circumentances 
'''