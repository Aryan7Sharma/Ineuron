class person:

    def age(self, curretn_year , year_of_birth):
        return curretn_year - year_of_birth

    def email_id_input(self, email_id ):
        print("take and mail id form a person and print it " , email_id)

    def ask_name(self):
        name = input("tell me your name ")
        return name

    def ask_dob(self):
        dob = input("tell me your date of birth ")
        return dob

sudh = person()
anuj = person()
gargi = person()
krish = person()
hitesh = person()

sudh.email_id_input("sudhanshu@ineron.ai")
print(sudh.ask_name())

print(hitesh.ask_dob())

