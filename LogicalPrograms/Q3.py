#Q3. Write a function that prints Armstrong Numbers from 1 to 500.
#By Hanumant More
for num in range(1,500 + 1):  
   sum = 0  
   temp = num  
   while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if num == sum:  
            print(num)  