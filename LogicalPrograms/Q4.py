#Q4. Write a function that prints Prime numbers from 1 to 500.
#By Hanumant More

def prime(x, y):
	prime_list = []
	for i in range(x, y):
		if i == 0 or i == 1:
			continue
		else:
			for j in range(2, int(i/2)+1):
				if i % j == 0:
					break
			else:
				prime_list.append(i)
	return prime_list
lst = prime(1, 500)
if len(lst) == 0:
	print("There are no prime numbers in this range")
else:
	print("The prime numbers in this range are: ", lst)
