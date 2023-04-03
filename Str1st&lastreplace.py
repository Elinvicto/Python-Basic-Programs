#Change a given string to a new string where the first and last characters have been exchanged.
#By Hanumant More
str1 = input("Enter your string : ")
def swap(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(swap(str1))