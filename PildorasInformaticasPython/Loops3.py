# Loops
#Do not forget to Encode the file to UTF-8

#range type 

#concatenate
'''
f'' = especial notation
{i} = print variables in f'' 
'''
for i in range(5):
    print(f'variable value {i}')
    
'''
begin=5
end=50
step=3
'''    
for i in range(5,50,3):
    print(f'variable value {i}')
    

#function len()
'''
returns the length
'''

valid=False

email=input('enter your mail address : ')

for i in range(len(email)):
    if email[i]=='@':
        valid=True
if valid==True:
        print('correct email')
else:
    print('incorrect email')