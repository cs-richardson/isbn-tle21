
ISBNsum = 0
ISBNdigit = str(input("Please enter your ISBN digit: "))

for i in range(len(ISBNdigit)): #looping i in range of how many digits there are in the ISBN digit
    ISBNsum = ISBNsum + (int(ISBNdigit[i]) * (i+1)) #the program multiplies the first digit of the ISBN by 1, the second by 2 and so on.  

if (ISBNsum % 11 == 0): #If the sum of the ISBN modulus 11 equals zero it is valid
    print ("Valid")
else:
    print ("Invalid") #If the sum of the ISBN modulus 11 does not equals zero it is invalid





