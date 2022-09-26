class bank: # parent class                               #Level 0
    def transaction(self):
        print("Tolat transaction value")
    def account_opening(self):
        print("This will show your account open status")

    def deposite(self):
        print("This will show your deposited amount")

class Hdfc_bank(bank): #child class     #Level 1
    def hdfc_to_icici(self):
        print("This will show you all the transaction happend to icici through hdfc")

class icici(Hdfc_bank): #Level 2
    pass

icici1=icici()
icici1.hdfc_to_icici()
icici1.deposite()
icici1.hdfc_to_icici()
icici1.account_opening()