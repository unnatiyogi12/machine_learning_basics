import string
import random
from pathlib import Path
import json

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():            
            with open(database) as fs:
                data = json.loads(fs.read())
        
        else:
            print("No such file exsist")

    except Exception as e:
        print(f"An Error occurs as {e}")

    # update function - y dummy data m jo data store h usko final database m daal deta h
    @classmethod
    def __update(cls):
        with open(Bank.database, "w") as fs:
            fs.write(json.dumps(Bank.data))
    
    @classmethod

    def __autogenerate(cls):
        alphabet = random.choices(string.ascii_letters, k = 4)
        numbers = random.choices(string.digits, k= 4)
        special = random.choices("!@#$%^&*", k = 2)

        id = alphabet + numbers + special
        random.shuffle(id)
        return "".join(id)



    # creating account
    def createaccount(self):
        info = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "gmail": input("Enter your gmail: "),
            "pin": int(input("Enter your 4-digit pin: ")),
            "accountNO": Bank.__autogenerate(),
            "Balance": 0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("\n❌ Sorry, you cannot create an account.\n")
            return

        print("\n✅ Your account created successfully!\n")

        for key, value in info.items():
            print(f"{key} : {value}")

        print("\n👉 Please note down your account number.\n")

        Bank.data.append(info)
        Bank.__update()
         # yaha se jo data user ne enter kiya use dummy data m append kiya h mtlb usme push kiya
        # phir update ko call kiya


    # depositing money
    def depositmoney(self):
        accnumber = input("Enter your account number :- ")
        pin = int(input("Enter your pin :- "))

        userdata = [i for i in Bank.data if i['accountNO'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")
        
        else:
            amount = int(input("Enter amount you want to deposit :- "))
            if amount > 10000 or amount < 0:
                print("Sorry you cannot deposit")
            
            else:
                userdata[0]['Balance'] += amount
                Bank.__update()
                print("Money deposit successfully !!")


    # withdrwaing money
    def withdrawmoney(self):
        accnumber = input("Enter your account number :- ")
        pin = int(input("Enter your pin :- "))

        userdata = [i for i in Bank.data if i['accountNO'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")
        
        else:
            amount = int(input("Enter amount you want to withdraw :- "))
            if userdata[0]['Balance'] < amount:
                print("Sorry you dont have enough money")
            
            else:
                userdata[0]['Balance'] -= amount
                Bank.__update()
                print("Money withdraw successfully !!")


    def details(self):
        accnumber = input("Enter your account number :- ")
        pin = int(input("Enter your pin :- "))

        userdata = [i for i in Bank.data if i['accountNO'] == accnumber and i['pin'] == pin]
        print("Your information are given below : \n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    
    def updatedetails(self):
         accnumber = input("Enter your account number :- ")
         pin = int(input("Enter your pin :- "))

         userdata = [i for i in Bank.data if i['accountNO'] == accnumber and i['pin'] == pin]

         if not userdata:
            print("No such user found")
            return

         user = userdata[0]

         print("You cannot change age, account number, or balance")
         print("Fill details or press Enter to skip")

         new_name = input("Enter new name: ")
         new_gmail = input("Enter new gmail: ")
         new_pin = input("Enter new pin: ")

         if new_name != "":
           user['name'] = new_name

         if new_gmail != "":
                user['gmail'] = new_gmail

         if new_pin != "":
                if len(new_pin) == 4 and new_pin.isdigit():
                    user['pin'] = int(new_pin)
                else:
                    print("Invalid pin — keeping old pin")

         Bank.__update()
         print("Details updated successfully!")

    
    # to delete the account1

    def Delete(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("sorry no such data exist ")
        else:
            check = input("press y if you actually want to delete the account or press n")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0]) #list k ander jo dictionary h use access krenge then change krenge
                Bank.data.pop(index)
                print("account deleted successfully ")
                Bank.__update()

# all operations
user = Bank()

print("Enter 1 for creating account :-")
print("Enter 2 for depositing in the account :-")
print("Enter 3 for withdrawing from an account :-")
print("Enter 4 for showing the account details :-")
print("Enter 5 to update the details :-")
print("Enter 6 to delete the account :-")

choice = int(input("Enter your choice :- "))

if choice == 1:
    user.createaccount()

if choice == 2:
    user.depositmoney()

if choice == 3:
    user.withdrawmoney()

if choice == 4:
    user.details()

if choice == 5:
    user.updatedetails()

if choice == 6:
    user.Delete()