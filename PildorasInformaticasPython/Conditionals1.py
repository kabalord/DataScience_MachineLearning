#Conditionals

#comparator operators

'''
>
>
==
>=
<=
!=

Do not forget to Encode the file to UTF-8

Everything write in the input is always string

'''



print("Classement student note program :")

student_note=int(input("enter the note :"))

def evaluation(note):
    value="approved"
    if note < 5:
        value="not-approved"
    return value

print(evaluation(student_note))