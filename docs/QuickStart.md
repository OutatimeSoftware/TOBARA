# TOBARA Quick Start.

TOBARA is a Python library designed for the manipulation of Boolean algebra that makes us easy the use of some toolkits like truth tables, Kmaps, etc. To start using TOBARA you only need to know the basic concepts of the Boolean algebra to be able to represent correctly what we can observe, so first lets try to see it how the essential parts work: the number of variables and the minterms.

To define a Boolean function we need to establish the number of variables that conform it, you can get this information if you observe the number of letters that are involved in your Boolean function, on the other hand, the minters are the Boolean representation of those variables.

If you think about it, there is a really simple relation between the variables and the minterms. Every time you add a variable you have to consider two other ways to form a term, but let look it in a more way: 



```python
tabla = getTable( 1,[ ] )
print( "1 variable" )
for line in tabla:
    print( line )
print()

tabla = getTable( 2,[ ] )
print( "2 variables" )
for line in tabla:
    print( line )
print()
    
tabla = getTable( 3,[ ] )
print( "3 variables" )
for line in tabla:
    print( line )
print()
    
tabla = getTable( 4,[ ] )
print( "4 variables" )
for line in tabla:
    print( line )
```

    1 variable
    [0, 0]
    [1, 0]
    
    2 variables
    [0, 0, 0]
    [0, 1, 0]
    [0, 1, 0]
    [1, 1, 0]
    
    3 variables
    [0, 0, 0, 0]
    [0, 0, 1, 0]
    [0, 0, 1, 0]
    [0, 1, 1, 0]
    [0, 0, 1, 0]
    [1, 0, 1, 0]
    [0, 1, 1, 0]
    [1, 1, 1, 0]
    
    4 variables
    [0, 0, 0, 0, 0]
    [0, 0, 0, 1, 0]
    [0, 0, 0, 1, 0]
    [0, 0, 1, 1, 0]
    [0, 0, 0, 1, 0]
    [0, 1, 0, 1, 0]
    [0, 0, 1, 1, 0]
    [0, 1, 1, 1, 0]
    [0, 0, 0, 1, 0]
    [1, 0, 0, 1, 0]
    [0, 1, 0, 1, 0]
    [1, 1, 0, 1, 0]
    [0, 0, 1, 1, 0]
    [1, 0, 1, 1, 0]
    [0, 1, 1, 1, 0]
    [1, 1, 1, 1, 0]
    
