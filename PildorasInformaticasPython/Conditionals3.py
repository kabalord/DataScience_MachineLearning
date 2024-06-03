#Conditionals

'''
Do not forget to Encode the file to UTF-8

- logic operators
- use of concatenated comparison operators

age=int(input('give an age : '))

if age < 100 and age > 0:
    print('correct age')
else:
    print('incorrect age')
    
'''    

president_salary=int(input('enter president salary : '))
print('president salary : ' + str(president_salary))

director_salary=int(input('enter director salary : '))
print('director salary : ' + str(director_salary))

manager_salary=int(input('enter manager salary : '))
print('manager salary : ' + str(manager_salary))

analyst_salary=int(input('enter analyst salary : '))
print('analyst salary : ' + str(analyst_salary))


if analyst_salary < manager_salary < director_salary < president_salary:
    print('everything is working properly')
else:
    print('something is wrong with this company')