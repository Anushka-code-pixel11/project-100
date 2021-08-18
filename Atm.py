class Atm(object):
    def __init__(self, cardnumber, pinnumber):
        self.cardnumber: cardnumber
        self.pinnumber: pinnumber

    def CashWithdrawl():
        print("cash is withdrawn")

    def BalanceEnquiry():
        print("enquiry succesfully done")

    def AtmCardNumber():
        print("Enter Your Atm Card Number")

    def PinNumber():
        print("enter your pin")

mya = Atm("12339428392", "110")
print(mya.cardnumber)
mya.CashWithdrawl()
