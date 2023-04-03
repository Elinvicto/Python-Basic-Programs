#Q21. A program to read a file in reverse order. The last sentence should be read first and continue till the first sentence is read.
#Hanumant More
textfile = str(input("Enter the string - "))
lines = textfile
for line in reversed(lines):
    print(line)
    print("\b\b\b")