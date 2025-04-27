from datetime import date
name = input("Enter your name: ")
year_of_birth = int(input("Enter your birth year: "))
todays_date = date.today()
current_year = todays_date.year
age = current_year - year_of_birth
print("The age is:", age)
if age>60:
    print("The person is a senior citizen and eligible to vote")
elif age > 18 and age <= 60:
     print("The person is an adult and eligible to vote")
elif age > 5 and age <= 16:
    print("The person is a kid and ineligible to vote")
else:
    print("The person is a toddler and ineligible to vote ")
    
    
    
    
    
    
    
    
    
    
    
    
