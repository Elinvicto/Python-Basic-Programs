#Q11. Function to find the sum of digits of a number.
#By Hanumant More
n = input("Enter the number: ")
def dsum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   

print(dsum(n))