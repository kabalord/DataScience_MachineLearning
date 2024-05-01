# What are the lists?

'''
Data structure that allows us to store a large number of values 
(equivalent to arrays in other programming languages).

In Python, lists can hold different types of values
(in other languages this is not the case with arrays).

They can be expanded dynamically by adding new elements
(another novelty compared to arrays in other languages).

'''

'''
Syntax of lists

list_name=[elem1,   elem2,   elem3,   etc..]
           index0   index1   index2   index3
'''

'''
Do not forget to Encode the file to UTF-8
'''
#multiple data types in the same objet
mylist=['walter', 'roa', 'serrano', 25, 'July', 1986, 'Colombia', True, 78.56]

#all list
print(mylist[:]) 

#access per position
print(mylist[2])

#inverse list
print(mylist[-3])

#access to a list range (inclusif and exclusif)
print(mylist[0:6])

#same result starting with zero par default 
print(mylist[:7])

#starting with other index
print(mylist[5:8])

#access to last two elements among 8 (from 6 to end)
print(mylist[6:])

#append to add elements at the end of the list
mylist.append('new')
print(mylist[:])

#to add in a different position
#mylist.insert(index,'new element')
mylist.insert(5,'different position')
print(mylist[:])

#to add many elements
mylist.extend(['element1', 'element2', 'element3', 'element4',])
print(mylist[:])

#to find an element index
print(mylist.index('roa')) 
#if we have two or more elements with same content the index from first element will be returned

#check whether or not element is on the list
print('walter' in mylist) #true or false

#to remove elements
mylist.remove('walter')
print(mylist[:])

#to eliminate the element on a list 
mylist.pop()
print(mylist[:])

#concatenate lists
mylist1=['elem1', 'elem2', 'elem3',]

mylist2=['elem4', 'elem5', 'elem6',]

mylist3=mylist1+mylist2
print(mylist3[:])

#repeat list (multiply)
mylist4=[1,2,3] * 3
print(mylist4[:])
