import check_up_price as price
import time_slot as slot
import random
print("welcome to the Medanta's appointment interface...")
print("Please, Enter the required details below :-",'\n')

name = input("Enter the name of patient: ")
mobile_no = int(input("Enter the mobile number: "))
Address = input("Enter the address of patient: ")

with open("details.txt","w") as f:
    f.write(name + "\n")
    f.write(str(mobile_no) + "\n")
    f.write(Address + "\n")

print("Check ups list : ")
print('''
         CBC ,
         BMP ,
         CMP ,
         Thyroid Profile Test ,
         LFT ,
         Coagulation Panel Test  ,
         Vitamins and minerals Levels ,
         Electrolyte Test ,
         Lipid profile ,
         Complete Vitamin Panel ,
         chest X-rays ,
         Typoid test ,
         Malaria test ,
         FBS ,
         Diabetes Panel Basic ,
         Diabetes Profile - Advance ''')
type = input("Select the type of check up :- ")
print("The price of",type,"is",price.checkup_price[type])

res = input("Do you want to book a slot ? ")
if(res=="yes"):
    a = random.randint(0,3)
    b = random.randint(0,1)
    print("Empty date slot is : ",slot.slot_date[a])
    print("Empty time slot is : ",slot.slot_time[b])
else:
    print("No appointment booked!")
print("Thanks!, for visiting the interface...")