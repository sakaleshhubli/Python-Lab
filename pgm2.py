n=int(input("the number of students="))
topper=0
low_scorer=100
for i in range(0,n):
   name=input("enter the students name=")
   USN=input("enter the student's USN=")
   m1=int(input("enter the student's marks1="))
   m2=int(input("enter the student's marks2="))
   m3=int(input("enter the student's marks3="))
   total_marks=m1+m2+m3
   per=total_marks/3
   if(per>topper):
       topper=per
       stud=name
   if(low_scorer>per):
       low_scorer=per
       lowstud=name
   print("STUDENTS DETAILS")
   print(f"\n Name=",name)
   print(f"\n USN=",USN)
   print(f"\n total_marks=%.2f"%total_marks)
   print(f"\n percentage=%2f"%per)
print(f"{stud} has scored %.2f percentage,which is the highest"%topper)
print(f"{lowstud}has scored %.2f percentage,which is the lowest"%low_scorer)










''''''

