class bank: # parent class  1                             #Level 0
    def transaction(self):
        print("Tolat transaction value")
    def account_opening(self):
        print("This will show your account open status")
    def deposite(self):
        print("This will show your deposited amount")
    def test(self):
        print("this is a test method from bank")

class Hdfc_bank():   # parent class  2
    def hdfc_to_icici(self):
        print("This will show you all the transaction happend to icici through hdfc")
    def test(self):
        print("this is a test method from Hdfc_bank")

class ineuron_bank:
    def acc_sta(self):
        print("This is Ineuron Bank Class")

class icici(bank,Hdfc_bank,ineuron_bank): # inherated more than one class at a time (multiple inheritance)
    pass

icici1=icici()
icici1.hdfc_to_icici()
icici1.account_opening()
icici1.deposite()
icici1.transaction()
icici1.test()
icici1.acc_sta()