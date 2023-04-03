#Q17. Take a list and return a new list with unique elements of the first list. Import the module and input a list to find the unique elements in a list.
#By Hanumant More
from collections import Counter
input_list = [1, 2, 2, 5, 8, 4, 4, 8]
items = Counter(input_list).keys()
print("No of unique items in the list are:", len(items))