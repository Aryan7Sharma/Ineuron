class ineuron:
    def student(self):
        print("Print the all details of the student")
    def achiverse(self):
        print("Print the list of all achivers")
    def hall_of_fame(self):
        print("Print everyone from hall of fame")

class ineuron_vision(ineuron):
    def student(self): # method overriding
        print("these are the filtered student list")


i=ineuron_vision()
i.student()
