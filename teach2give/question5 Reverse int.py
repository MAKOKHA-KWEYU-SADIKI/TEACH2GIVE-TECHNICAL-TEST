#Write a program that takes an integer as input and returns an integer with reversed digit
#ordering
inpput=int(input("enter the integer to reverse :"))
reversed_no= 0
while inpput!=0:
    digitt=inpput%10
    reversed_no=reversed_no*10+digitt
    inpput //= 10
print(reversed_no)    

