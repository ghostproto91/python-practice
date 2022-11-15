#prime number check
n=int(input('Enter the number to be checked:'))

half_num=(n//2)
divisors=0
i=1
while[True]:
    if n%i==0:
        divisors+=1
        if divisors==2:
            break
    i+=1
    if i>half_num:
        break
if divisors>=2:
    print(f'{n} is a composite number!')
else:
    print(f'{n} is a prime number!')
