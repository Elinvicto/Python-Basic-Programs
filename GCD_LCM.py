#Q12. Function to find GCD/LCM of 2 numbers.
#By Hanumant More
def gcd(a,b):
	if a == 0:
		return b
	return gcd(b % a, a)
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a,b))
else:
    print('not found')
def lcm(a,b):
	return (a / gcd(a,b))* b
print('LCM of', a, 'and', b, 'is', lcm(a, b))