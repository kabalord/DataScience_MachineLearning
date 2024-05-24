# Dictionnaires - HashMaps

'''
What are dictionaries ?

A data structure that allows us to store values of different types.
(integers, decimal text strings) and even lists, tuples and other dictionaries.

The main feature of dictionaries is that data is stored in association with a key, 
so that for each stored item a key:value association is created.

The stored elements are not ordered. 

The order is irrelevant when storing information in a dictionary.
'''

'''
Do not forget to Encode the file to UTF-8
'''

# key:value (key is unique)
mydictionary={"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}

# to print all mydictionary
print(mydictionary)

# if I want to search an element you can use the key :
print(mydictionary["Francia"])

# how to add new elements to the dictionary
mydictionary["Colombia"]="Medellin"
print(mydictionary)

# how to correct or re-assign
mydictionary["Colombia"]="Bogota"
print(mydictionary)

#how to eliminate an element
del mydictionary["Reino Unido"]
print(mydictionary)

# I can use doesn't matter type
mydictionary[99]="new1"
mydictionary["new2"]=00
print(mydictionary)

#you can use a tuple to assign the values
mytuple=("España", "Francia", "Reino Unido", "Alemania")
my_dc={mytuple[0]:"Madrid", mytuple[1]:"Paris"}
print(my_dc)

#to acces 
print(my_dc["Francia"])

#how to stock a tuple in a dictionary
my_dic={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":(1991,1992,1993,1996,1997,1998)}
print(my_dic)

#how to use a dictionary inside another dictionary
my_dic_in={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":(1991,1992,1993,1996,1997,1998)}}
print(my_dic_in["anillos"])

#methods

print("keys   :  ",mydictionary.keys())
print("values :  ",mydictionary.values())
print("len    :  ",len(mydictionary))
