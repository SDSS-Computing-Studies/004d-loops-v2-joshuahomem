#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""
num=int(input("Enter an integer smaller than 10: "))
if num>=10:
    print("That integer is larger than 10")
    quit()
digit="1"
a=0
b=0
c=0
d=0
for i in range(1,num+1):
    
    b=int(i*digit)
    d=b+c
    c=d
    
    
print("the sum of the series is "+str(d))
