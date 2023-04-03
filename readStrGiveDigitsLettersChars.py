#Q7. Accept a string and calculate the number of digits, letters and other characters.
#By Hanumant More
s = str(input("Input a string : "))
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else :
        print("Characters ",len(c))
print("Letters", l)
print("Digits", d)