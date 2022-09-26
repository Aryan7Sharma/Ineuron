class Person1:
    def __init__(self, name, email, surname, dob):#self pointer is point to a person class you can use any name instead of self
        self.name = name
        self.yob = dob
        self.surname = surname
        self.emailid = email
obj = Person1 ("aryan", "aryan@gmail.com", "sharma", 2003)
print(obj.name+obj.surname, obj.emailid)
print(obj.yob)
print(type(obj))

s="aryan"
print(help(reversed))



