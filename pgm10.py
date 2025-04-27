#to find the largest of 3 numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
b = int(input("Enter the third number: "))

largest = 0
if(a>b and a>c):
    largest = a
elif(b>c):
    largest = b
else:
    largest = c

print(largest, "is the largest of three numbers")