#fibonacci series

n = int(input("Enter the length of series: "))
n1 = 0
n2 = 1
next_number = n2 
temp = 1

while temp <= n:
	print(next_number, end=" ")
	temp += 1
	n1, n2 = n2, next_number
	next_number = n1 + n2
print()