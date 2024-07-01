# Loops Continue, pass and else
#Do not forget to Encode the file to UTF-8

'''
"Continue = skip to the next iteration of a loop"

"Pass = returns null in the loop, it's as if the loop does not execute"
In essence, pass helps maintain the program's structure 
when you don't have any code to execute in certain blocks, 
ensuring that the program remains syntactically correct.

"Else = is used the same way as with an if conditional"
'''

##Continue

for letter in 'python':

    if letter == 'y':
        continue
    print('this is : ' + letter)
    

name='tech pills'
print(len(name))


counter=0
for i in name:
    if i==' ':
        continue
    counter+=1
print(counter)


##Pass
'''
#Defining a minimal class or function:
class MyClass:
    pass # to implement later

#Creating placeholders for code to be implemented later:
def my_function():
    pass

#In loops:
for i in range(10):
    if i % 2 == 0:
        pass  # No action is needed for even numbers
    else:
        print(i)

#In conditionals:        
if condition:
    pass  # To be handled later
else:
    print("Condition is False")        

'''    
 
##Else

email=input('Enter your mail, please : ') 
 
for i in email:
    if i=='@':
        at=True
        break;
else:

    at=False
print(at)
 