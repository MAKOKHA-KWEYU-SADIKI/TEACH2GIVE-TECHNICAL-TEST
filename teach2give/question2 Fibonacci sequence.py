#Write a program to generate the Fibonacci
#sequence up to 100.
seq=[0,1]
def feb():
   while len(seq)<100: 
        nextt=seq[-1]+seq[-2]
        seq.append(nextt)
        for i in seq:
               print(i)
feb()


