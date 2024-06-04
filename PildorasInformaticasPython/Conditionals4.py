#Conditionals

'''

logic operators and / or / in

'''

print('scholarship programme year 2024')


school_distance=int(input('enter the distance to school in km :'))     
print(school_distance)

number_of_siblings=int(input('enter the number of siblings :'))
print(number_of_siblings)

family_salary=int(input('enter gross annual salary :'))
print(family_salary)


if school_distance > 40 and number_of_siblings > 2 or family_salary <= 7000:
    print('you are entitled to a scholarship')
else:
    print('you are not entitled to a scholarship')





print('electives year 2024')
print('electives : programming - algorithms - data structures') 
option=input('chose the one for you :')

elective=option.lower()

if elective in ('programming', 'algorithms', 'data structures'):
    print('you have chose ' + elective)
else:
    print("elective isn't available")

