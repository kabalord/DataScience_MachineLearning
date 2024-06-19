# Loops
#Do not forget to Encode the file to UTF-8

#print on a single line

for i in [1,2,3,4,5]:
    print('hello', end=' ')
    
    

counter=0
myemail=input('enter your email : ')

for i in myemail:
    if i=='@' or i=='.':
        counter+=1
        
if counter==2:
    print('correct email address')
else:
    print('incorrect email address')


for i in range(5):
    print(i)