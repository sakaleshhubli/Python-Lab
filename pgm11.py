#to check the armstrong number

num = int(input("Enter the number: "))
sum = 0
temp = num
while temp>0:
    rem = temp%10
    sum += rem**3
    temp // 10
if num == sum:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")