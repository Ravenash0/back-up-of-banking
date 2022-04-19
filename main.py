def text_box_gap():
    print("""""")

#AHHHHHHHHHHHHHHHHHHHHHHHHH
def Deposit():
    Add = open("moeny.txt", "r")
    Adding = int(input("what amount of cash would you like to add: "))
    FileLines = Add.readlines()
    print(FileLines)
    intCash = (FileLines[len(FileLines) - 1])
    print(intCash)
    print(type(intCash))
    curentbal = get_Balance_and_Transaction(intCash)
    print(curentbal)
    print(type(curentbal))
    intFileLines=int(curentbal)
    newBal = (intFileLines + Adding)
    print(intFileLines)
    Add.close()
    Add = open("moeny.txt", "a")
    Add.writelines("\n" + str(newBal))
    Add.close()
    Add = open("moeny.txt", "r")
    Add = Add.readlines()
    print(F"you have added {Adding}$ to the bank, you now have {newBal}")


def get_Balance_and_Transaction(BalanceString):
    curentbal = int(BalanceString[8:BalanceString.find("type")].strip())
    TransType = (BalanceString[BalanceString.find("type") + 5:].strip())
    return curentbal, TransType
    


try:
    User = open("Username.txt", "r")
    User = User.readline()
    print(F"Welcome back to the bank {User}")

except:
    User = open("Username.txt", "w")
    User.write(input("what is thy name?: "))
    User.close()
    User = open("Username.txt", "r")
    User = User.readline()
    print(F"Welcome to the bank {User}")

try:
    Cash = open("moeny.txt", "r")
except:
    Cash = open("moeny.txt", "a")
    Cash.write("balance: 100 type: deposit")
    Cash.close()
    Cash = open("moeny.txt", "r")

    Cashread = Cash.readlines()
    print(Cashread)
    intCash = (Cashread[len(Cashread) - 1])
    curentbal = int(intCash[8:intCash.find("type")].strip())
    curentbal, TransType = get_Balance_and_Transaction(intCash)
    text_box_gap()
    print(F"We are starting you off with {curentbal} dollars")
    print(TransType)

Deposit()
