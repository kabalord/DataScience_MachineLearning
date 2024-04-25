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
    