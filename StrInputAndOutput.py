#Read a string from user. Replace the occurrence of first character of the word with "$" except the first word.
#By Hanumant More
lis = []
s=input("Enter String: ")
for ch in s:
    if ch in lis:
        lis.append('$')
    else:
        lis.append (ch)
print(''.join(str(i) for i in lis))