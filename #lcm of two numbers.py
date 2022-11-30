#lcm of two numbers
a=int(input("Enter a positive integer"))
b=int(input("Enter another positive integer"))

min_divisor = (lambda: b, lambda: a)[a > b]()
while(1):
    if ((min_divisor%a==0) & (min_divisor%b==0)):
        lcm=min_divisor
        break
    min_divisor+=1
print ('The lcm of ',a ,'and',b ,"is",lcm)
     
