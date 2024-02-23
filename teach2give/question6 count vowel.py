#Write a program that counts the number of vowels in a sentence.
string=input("enter your string :")
count=0
vowel="a","e","i","o","u"
for i in string:
    for r in vowel:
        if r==i:
            count+=1
print(count)        