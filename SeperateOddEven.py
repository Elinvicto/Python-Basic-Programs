#Q9.A program that accepts a range of numbers (n to m) and list down all the even/odd numbers to be printed in a comma separated sequence.
#By Hanumant More
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num % 2 != 0:
        print(num, end = ", ")