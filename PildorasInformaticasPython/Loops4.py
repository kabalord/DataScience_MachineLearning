# Loops while
#Do not forget to Encode the file to UTF-8

'''
While loop : Indeterminate because we don't previously know the number of execution times

#Syntax

while condition:
    loop body
'''

i=1
while i<=10:
    print('execution time ' + str(i))
    i+=1
print('is the 10th execution the loop is finish')

#Indeterminate example
age=int(input('enter you age : '))
while age<5 or age>100:
    print('age no valid')
    age=int(input('enter you age : '))
print('thanks, your age is ' + str(age))

#square root program

import math

number=int(input('enter the number to calculate sqrt : '))

attemps=0
while number<0:
    print('is not possible to calculate sqrt from a negative number.')
    
    if attemps==2:
        print('too many attemps, the program is end.')
        break;
    
    number=int(input('enter the number to calculate sqrt : '))
    if number<0:
        attemps+=1

if attemps<2:
    solution=math.sqrt(number)
    print('the sqrt of '+str(number)+' is '+str(solution))