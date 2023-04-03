#Q1. Create a function that returns a,b and a+b
#By Hanumant More
def add(a, b):
    result = a + b
    return result
a = int(input("Enter number : "))
b = int(input("Enter number : "))
print("Entered numbers are : ",a ,"and",b)
print("Addition of entered numbers is : ",add(a, b))