#What are the functions?

'''
A set of grouped lines of code (code block) that function as a unit
that function as a unit performing a specific task.

Python functions can have parameters / arguments.

Python functions can return values.

Functions are also called 'methods' when they are defined within a class.

'''

'''
Utility
Code reuse (when or if necessary)
'''

'''

'''

#function begin
def function():
    print("here you can write something")#it is necessary to indent 
#you need to always call the function
function()
function()
function()     


def Suma():
    num1=5
    num2=7
    print(num1+num2)

Suma()

#with parameters
def SumaWithParameters(num1, num2):
    print(num1+num2)

SumaWithParameters(5,8)
SumaWithParameters(2,3)
SumaWithParameters(35,358)

#function with return
def SumaConReturn(num1,num2):
    return num1 + num2

variable = SumaConReturn(5,6)
print(variable)
    
#function with return in variable
def SumaConReturn(num1,num2):
    result = num1 + num2
    
    return result

variable = SumaConReturn(15,16)
print(variable)