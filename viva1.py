#number palindrome

num = int(input("Enter the number: "))
temp = num
rev = 0

while num>0:
    digit = num%10
    rev = rev*10 + digit
    num = num//10
if temp==rev:
    print("It is a palindrome")
else:
    print("Not a palindrome")