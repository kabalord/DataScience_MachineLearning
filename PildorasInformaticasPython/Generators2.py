# Generators

#Do not forget to Encode the file to UTF-8

#New instruction yield from

'''
Utility:

"Simplify the code of generators when using nested loops."

* in Python function definitions is used to capture an arbitrary number of positional arguments into a tuple.  

'''

## 1 example simple loop
def return_cities(*cities):
    for element in cities:
        yield element
    

returned_cities=return_cities('Madrid', 'Barcelona', 'Bilbao', 'Valencia')

print(next(returned_cities))

print(next(returned_cities))


## 2 example nested loop 
def return_cities_nested(*cities):
    for element in cities:
        for subelement in element:
            yield subelement
            
returned_cities_nested=return_cities_nested('Madrid', 'Barcelona', 'Bilbao', 'Valencia')

print(next(returned_cities_nested))

print(next(returned_cities_nested))

## 3 example yield from

def return_cities_yield_from(*cities):
    for i in cities:
        yield from i
        
returned_cities_yield_from=return_cities_yield_from('Barcelona', 'Bilbao', 'Valencia')

print(next(returned_cities_yield_from))
print(next(returned_cities_yield_from))
print(next(returned_cities_yield_from))
print(next(returned_cities_yield_from))
print(next(returned_cities_yield_from))
print(next(returned_cities_yield_from))
print(next(returned_cities_yield_from))
print(next(returned_cities_yield_from))
print(next(returned_cities_yield_from))
