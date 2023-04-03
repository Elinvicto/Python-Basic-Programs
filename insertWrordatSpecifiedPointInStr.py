#Q22. Insert a sentence into a specified position of a file.
#By Hanumant More
def insert(x, n_list, pos):
    return n_list[:pos-1]+[x]+n_list[pos-1:]
n_list = [1,1,2,3,4,4,5,1]
print("Original list:") 
print(n_list)
kth_position = 3
x = 12
result = insert(x, n_list, kth_position)
print("\nAfter inserting an element at kth position in the said list:")
print(result)