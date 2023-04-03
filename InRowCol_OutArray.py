#Q8. A program that takes two digits m(row) and n (column) as input and generates a Two-dimensional array. Read the elements and display the array.
#By Hanumant More
m=int(input("Row:"))
n=int(input("Column:"))
result=[[0 for col in range(n)] for row in range(m)]
for row in range(m):
    for col in range(n):
        result[row][col]=row*col
print(result)