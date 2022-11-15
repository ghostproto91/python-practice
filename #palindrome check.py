#palindrome check

palin_str=input("Enter the number/word:")

palin_str = palin_str.casefold()

palin_str_reverse = reversed(palin_str)

if list(palin_str) == list(palin_str_reverse):
    print (palin_str , 'is a palindrome sequence')
else:
    print (palin_str , 'is not a palindrome sequence')
