class Person2:
    def __init__(aryan, name, email, surname, dob):#self pointer is point to a person class you can use any name instead of self
        aryan.name = name
        aryan.yob = dob
        aryan.surname = surname
        aryan.emailid = email

    def age(self, cy):
        age=cy-self.yob
        return age

    def uppercase(self,string):
        ans=""
        for i in range(len(string)):
            assci=ord(string[i])-32
            ans+=chr(assci)
        return ans

obj = Person ("aryan", "aryan@gmail.com", "sharma", 2003)
print(obj.name+obj.surname, obj.emailid)
print(obj.yob)
print(type(obj.yob))
aryan = Person("aryan", "aryan@gmail.com", "sharma", 2003)
aryan.age(2022)
print(aryan.age(2022))
print(aryan.uppercase("aryan"))


def uppercase(self, string):
    ans = ""
    for i in range(len(string)):
        assci = ord(string[i]) - 32
        ans += chr(assci)
    return ans