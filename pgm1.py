#pgm to read the student details and display with marks and percentage
name = input("Enter the student's name: ")
USN = input("Enter the student's USN: ")
Marks1 = int(input("Enter the students marks1: "))
Marks2 = int(input("Enter the students marks2: "))
Marks3 = int(input("Enter the students marks3: "))
Total_Marks = Marks1 + Marks2 + Marks3
per = Total_Marks/3

print("Student Details")
print("\n Name:", name)
print("\n USN:", USN)
print("\n Total marks obtained: %.2f" %Total_Marks)
print("\n Percentage is: %.2f" %per)