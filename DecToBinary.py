#Q15. Convert decimal to binary using recursion.
#By Hanumant More
n = int(input("Enter decimal number: "))
def binary(n):
   if n > 1:
       binary(n//2)
   print(n % 2,end = '')
print("Converted binary number is:", end = ' ')
binary(n)