# What are the tuples?

'''
Tuples are immutable lists, i.e. they cannot be modified after their creation.

    - They do not allow adding, deleting, moving elements, etc. (no append, extend, remove).
    - They do allow to extract portions, but the result of the extraction is a new tuple.
    - They do not allow searching (no index).
    - They do allow to check if an element is in the tuple.
    
Advantages of tuples over lists:

    - Faster 
    - Less space (more optimisation)
    - They format strings
    - They can be used as keys in a dictionary (lists cannot).
'''

'''
Syntax of tuples

tuple_name=(elem1,   elem2,   elem3,   etc..)
           index0   index1   index2   index3
'''

'''
Do not forget to Encode the file to UTF-8
'''

mytuple=('walter', 'roa', 'serrano', 25, 'July', 1986, 'Colombia', True, 78.56, 25)
print(mytuple[1])
print(mytuple[:])

#convert tuples to lists and vice versa 
my_list=['li1', 'li2', 'li3', 'li4', 'li5', 'li6']
print(my_list)
print('#my_list_to_tuple')
my_list_to_tuple=tuple(my_list)
print(my_list_to_tuple)

my_tuple=('tup1', 'tup2', 'tup3', 'tup4', 'tup5', 'tup6')
print(my_tuple)
my_tuple_to_list=list(my_tuple)
print('#my_tuple_to_list')
print(my_tuple_to_list)

#check if an element exists in a tuple 
print('tup1' in my_tuple)

#count how many times an element exists in a tuple
print(mytuple.count(25)) 

#check the length of a tuple
print(len(mytuple))

# create unit tuples , is mandatory
unitary_tuple=('unitary tuple',)
print(unitary_tuple)

# () are not mandatory 
this_is_tuple_too='walter', 'roa', 'serrano'
print(this_is_tuple_too)

print('# unpacking tuples it is the process that assigns the values on the right-hand side to the left-hand side variables.') 
print('# In unpacking, we basically extract the values of the tuple into a single variable.')
print('packvar1, packvar2, packvar3 = this_is_tuple_too')
packvar1, packvar2, packvar3 = this_is_tuple_too
print('packvar1:', packvar1)
print('packvar2:', packvar2)
print('packvar3:', packvar3)