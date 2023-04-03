#Q6. Merge two python dictionaries.
#By Hanumant More
Dictionary1={'Subaru','Rolls Royce','Hyundai','Honda','Genesis','Kia','Maruti','Lexus'}
Dictionary2={'Tesla','GMC','Hummer','Mercedes Benz','BMW','Audi','Jaguar','Jeep','Ford','Force','TATA','Mahindra'}
print("Contents of first dictionary are: ",Dictionary1)
print("Contents of second dictionary are: ",Dictionary2)
Dictionary1.update(Dictionary2)
print("Dictionary after updation: ",Dictionary1)