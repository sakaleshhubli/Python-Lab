#binomial coeff
n = int(input("Enter the n value: "))
r = int(input("Enter the r value: "))

def fact(x):
    if x ==1:
        return 1
    else:
        return x*fact(x - 1)
def bin_coeff(n,r):
    b = (fact(n))/(fact(n-r)*fact(r))
    return b

print("Binomial coefficient is:", bin_coeff(n,r))