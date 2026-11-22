from datetime import datetime,date
print("AGE CALCULATOR")
print("==============")
dob=input("Enter your birth date (DD-MM-YYYY):")
print()
tdate=date.today()
dob=datetime.strptime(dob,"%d-%m-%Y").date()
birthday=dob.replace(year=(tdate.year))
age = tdate.year - dob.year
if birthday > tdate:
    age = age - 1
live_days=tdate-dob
print(f"Today's date  : {tdate.strftime('%A, %d %B %Y')}")
print(f"Born on       : {dob.strftime('%A, %d %B %Y')}")
print(f"Age           : {age}")
print(f"Days lived    : {live_days.days}")
if birthday < tdate :
    birthday=dob.replace(year=(tdate.year+1))
    days_to_go = (birthday - tdate).days
    print(f"Next Birthday : {birthday.strftime('%A, %d %B %Y')} ")
    print(f"Days to go    : {days_to_go}")
elif birthday ==tdate:
    print("Today is your birthday! Happy Birthday")
else:
    birthday=dob.replace(year=(tdate.year))
    days_to_go = (birthday - tdate).days
    print(f"Next Birthday : {birthday.strftime('%A, %d %B %Y')} ")
    print(f"Days to go    : {days_to_go}")



