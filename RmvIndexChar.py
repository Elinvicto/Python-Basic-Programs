#Q3. Remove the nth index character from a non-empty string.
#By Hanumant More
new = input("Enter the string : ")
n = 3
newstr = " "
for char in range(0, len(new)):
    if(char != n):
        newstr += new[char]
print("String after removing",n, "character is:",newstr)
