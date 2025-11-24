date = input("Enter todays date(date month year) : ")
def date_and_time():
    splited_date = date.split(" ")
    slot_date = []
    for i in range(1,5):
        slot_date.append(str(int(splited_date[0]) + i)+ " " + splited_date[1]+" " + splited_date[2])
    return(slot_date)

slot_date = date_and_time()
slot_time = ["8 A.M. to 12 P.M.","1 P.M. to 6 P.M."]