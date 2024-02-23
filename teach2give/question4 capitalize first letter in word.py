#Write a program that accepts a string as input, capitalizes the first letter of each word in the
#string, and then returns the result string.

string=input("enter the string :")
word=string.split()
listt=[]
for i in word:
    i=i.capitalize()
    listt.append(i)
print(" ".join(listt))

 