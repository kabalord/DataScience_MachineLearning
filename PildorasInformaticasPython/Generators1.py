# Generators
#Do not forget to Encode the file to UTF-8

'''
- What are they?

"Structures that yield values from a function and store them in iterable objects (which can be iterated over)"

"These values are stored one at a time".

"Each time a generator yields a value, it remains in a stand-by state until the next value is requested. 
This feature is known as state suspension."


- How do they work?

##Traditional Function
Returns all at once: A traditional function computes its result and returns all of it at once.
Example: If you ask for a list of even numbers up to 10, it will give you the whole list [0, 2, 4, 6, 8, 10] in one go.

def get_even_numbers(limit):
    even_numbers = []
    for num in range(0, limit + 1, 2):
        even_numbers.append(num)
    return even_numbers

# Usage
print(get_even_numbers(10))
# Output: [0, 2, 4, 6, 8, 10]


##Generator
Returns one at a time: A generator yields items one by one, pausing after each one until the next one is requested.
Example: If you ask for even numbers up to 10, it will give you 0, then 2, then 4, and so on, each time you ask for the next number.

def even_numbers():
    num = 0
    while True:
        yield num
        num += 2

# Usage
gen = even_numbers()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 2
print(next(gen))  # Output: 4
# And so on...

Key Differences
Memory Usage: Generators are more memory efficient because they yield items one at a time, whereas traditional functions store all results in memory at once.
Execution: Traditional functions run to completion and return a result. Generators can pause and resume, making them suitable for large datasets or continuous streams of data.
So, a traditional function gives you everything at once, while a generator gives you one thing at a time, pausing between each one.

- What are they useful for?

- They are more efficient than traditional functions.
- Very useful with lists of infinite values.
- Under certain scenarios, it will be very useful for a generator to return values one by one.
 

- What is their syntax?
def even_numbers():
    num = 0
    while True:
        yield num
        num += 2
'''
##traditional function
def generaPares(limite):

    num=1    
    
    miLista=[]    
    
    while num<limite:
    
        miLista.append(num*2)
        num+=1
        
    return miLista
    
print(generaPares(10))



##generator
def generaPares(limite):

    num=1       
    
    while num<limite:
    
        yield num*2
        num+=1
        
devuelvePares=generaPares(10)

for i in devuelvePares:
    print(i)
    
    
##generator
def generaPares(limite):

    num=1       
    
    while num<limite:
    
        yield num*2
        num+=1
        
devuelvePares=generaPares(10)

print(next(devuelvePares))
print('here you can have code')
print(next(devuelvePares))
print('here you can have code')
print(next(devuelvePares))