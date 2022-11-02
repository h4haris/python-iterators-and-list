# Python - Iterators and Lists (Data Science Toolbox)
Python iterators and lists comprehensions experimentation for Data Science
 
## Using iterators in Python

### Introduction to Iterators

```bash
1. Iterate over a list
======================
employees = ['Nick', 'Lore', 'Hugo']
for employee in employees:
    print(employee)

2. Iterate over a string
========================
for letter in 'Hello':
    print(letter)

3. Iterate over a range
=======================
for i in range(4):
    print(i)
```

We can loop over such objects because they are special objects called iterables.

#### Iterators vs. iterables

**iterables**
- lists, strings, range objects, dictionaries and file connections
- an object that has an associated iter() method.
- applying iter() method to an iterable, creates an iterator object. 

This is actually what a for loop is doing: it takes an iterable, creates the associated iterator object, and iterates over it! 

**iterator**
- produce next value with next() method
- next method produces the consecutive values. 

```bash
1. Create an iterator and use next() to retrieve value
======================================================
word = 'Da'
it = iter(word)

next(it) => Output D
next(it) => Output a
next(it) => Output throw a StopIteration error

2. Iterating at once with *
===========================
# * referred as the splat operator
# unpacks all elements of an iterator or an iterable
# however, once we cannot do it again as there are no more values to iterate through! We would have to redefine our iterator again.

word = 'Data'
it = iter(word)
print(*it) => Output D a t a
print(*it) => Output No more values

3. Iterating over dictionaries
==============================
detail = {'name': 'haris', 'job', 'developer'}
for key, value in detail.items():
    print(key, value)

Output: job developer
        name haris

4. Iterating over file connections
==================================
file = open('file.txt')
it = iter(file)
print(next(it)) => Output: This is the first line
print(next(it)) => Output: This is the second line
```

### Playing with Iterators

1. enumerate()
    - will allow us to add a counter to any iterable
    - takes any iterable as argument, such as a list
    - returns a special enumerate object, which consists of pairs containing the elements of the original iterable, along with their index within the iterable

```bash
1. Using enumerate()
====================
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
e = enumerate(avengers)
print(type(e)) => Output: <class enumerate

# using list to turn this enumerate object into a list of tuples
e_list= list(e)
print(e_list) Output: [(0,'hawkeye'), (1,'iron man'), (2,'thor'), (3,'quicksilver')]

2. enumerate() and unpack
=========================
# enumerate object itself is also an iterable and we can loop over it

a. with default indexing start from 0
for index, value in enumerate(avengers):
    print(index, value)

Output: 0 hawkeye
        1 iron man
        2 thor
        3 quicksilver

b. with custom indexing using second argument start
for index, value in enumerate(avengers, start=10):
    print(index, value)

Output: 10 hawkeye
        11 iron man
        12 thor
        13 quicksilver
```

2. zip()
    - allow us to stitch together an arbitrary number of iterables
    - accepts an arbitrary number of iterables
    - returns an iterator of tuples
    - Zipping them together creates a zip object which is an iterator of tuples

```bash
1. Using zip()
==============
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
names = ['barton', 'stark', 'odinson', 'maximoff']
z = zip(avengers, names)
print(type(z)) => Output: <class zip

# using list to turn this zip object into a list of tuples
z_list= list(z)
print(z_list) Output: [('hawkeye', 'barton'), ('iron man', 'stark'), ('thor', 'odinson'), ('quicksilver', 'maximoff')]

2. zip() and unpack
===================
# zip object itself is also an iterable and we can loop over it

for z1, z2 in zip(avengers, names):
    print(z1, z2)

Output: hawkeye barton
        iron man stark
        thor odinson
        quicksilver maximoff

3. print zip with splat *
=========================
# using splat operator to print all the elements

z = zip(avengers, names)
print(*z)

Output: ('hawkeye', 'barton') ('iron man', 'stark') ('thor', 'odinson') ('quicksilver', 'maximoff')
```

### Using Iterators to load large files into memory

Dealing with large amounts of data
- too much data to hold in memory
- Solution: load data in chunks, perform operation on each chunk, then load new chunk
- specify the chunksize in pandas: read_csv

```bash
Iterating over large file data in chunks
========================================
# here read_csv call is an iterable in which each chunk will be a DataFrame
import pandas as pd
result = []
for chunk in pd.read_csv('data.csv', chunksize=1000):
    result.append(sum(chunk['x']))
total = sum(result)
print(total)

                    or

import pandas as pd
total = 0
for chunk in pd.read_csv('data.csv', chunksize=1000):
    total += sum(chunk['x'])
print(total)
```

## List comprehensions and generators

### List comprehensions

- create lists from other lists, DataFrame columns, etc.
- single line of code
- more efficient than using a for loop
- tradeoff: readability

#### List comprehensions required components 
- an iterable, 
- an iterator variable t(hat represents the members of the iterable) 
- an output expression.

```bash
SYNTAX
======
    output expression   for clause referencing 
              |         the original list
              |              |
              v              v
new_nums = [item + 1 for item in list]

1. For loop vs List comprehension
=================================
# EXAMPLE - Append 1 in each item of list
nums = [12, 8, 21, 3, 16]

a. Using for loop
for num in nums:
    new_nums.append(num + 1)
print(new_nums)

b. Using List comprehension
new_nums = [num + 1 for num in nums]
print(new_nums)

2. List comprehension with range()
==================================
result = [num for num in range(11)]
print(result)

3. Nested loops vs List comprehension
=====================================
# Create all pairs of numbers
Output: [(0,6),(0,7),(1,6),(1,7)]

a. Nested loops
pairs_1 = []
for num1 in range(0, 2):
    for num2 in range(6, 8):
        pairs_1.append((num1, num2))
print(pairs_1)

b. Using list comprehension
pairs_2 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]
print(pairs_2)
```

### Advanced comprehensions

Conditionals in comprehensions
- filter the output of a list comprehension using a conditional on the iterable
- condition the list comprehension on the output expression.

```bash
1. Conditionals on iterable
===========================
[num ** 2 for num in range(10) if num % 2 == 0]

Output: [0,4,16,36,64]

2. Conditionals on output expression
====================================
[num ** 2 if num % 2 == 0 else 0 for num in range(10)]

Output: [0,0,4,0,16,0,36,0,64,0]
```

Dictionary comprehensions
- use {} instead of []
- use : to separate keys/values

```bash
pos_neg = {num: -num for num in range(5)}
print (pos_neg)

Output: {0:0, 1:-1, 2:-2, 3:-3, 4:-4}
```

### Introduction to generator expressions

#### List comprehension vs generators
- list comprehension - returns a list
- Generators - returns a generator object
- both can be iterated over

#### Generator expressions
- replace [] with () to convert any list comprehension to generator object.

#### Generators object
- generator is like a list comprehension except it does not store the list in memory
- it does not construct the list, but is an object we can iterate over to produce elements of the list as required.
- help a great deal when working with extremely large sequences

#### Generator functions
- powerful and customizable way to create generators
- functions that produces generator objects when called
- defined like a regular function - def
- instead of returning values using return, they yield sequence of values
- generates a value with yield keyword

#### Example
When iterating over a dictionary with .items(), or using the range() function, python creates generators for us behind the scenes.

```bash
1. Printing values from generators
==================================
result = (num for num in range(6))
for num in result:
    print (num)

Output: 0
        1
        2
        3
        4
        5

2. Create list from generators
==============================
# pass a generator to the function list to create the list
result = (num for num in range(6))
print(list(result))

Output: [0,1,2,3,4,5]

3. Using lazy evaluation
========================
# pass a generator to the function next in order to iterate through its elements
# example of lazy evaluation, whereby the evaluation of the expression is delayed until its value is needed.
result = (num for num in range(6))
print(next(result))  => Output: 0
print(next(result))  => Output: 1
print(next(result))  => Output: 2

4. Conditionals in generator expressions
========================================
even_nums = (num for num in range(10) if num % 2 == 0)
print(list(even_nums))

Output: [0,2,4,6,8]

5. Build a Generator function
=============================
# produces a generator object that generates integers 0 though n

def num_sequence(n):
    """Generate values from 0 to n."""

    i = 0
    while i < n:
        yield i
        i += 1

# first time the generator object is called, it yields i equal to 0. 
# then adds 1 to i and will then yield next value on the next iteration and so on
# when loop end then the generator ceases to yield values

6. Using a Generator function
=============================
result = num_sequence(5)
print(type(result))

Output: <class generator

for item in result:
    print (item)

Output: 0
        1
        2
        3
        4
```

**Generators for the large data limit**
- we can use generator to load file line by line. [Like an iterator which load file in chunks]
- Works on streaming data, that is, if new lines are being written to the file we're reading. 
- reading and processing the file until there are no lines left for it to read.

**opening a file connection with context manager**

The command *with open('datacamp.csv') as datacamp* binds the csv file 'datacamp.csv' as datacamp in the context manager. 

Here, the with statement is the context manager, and its purpose is to ensure that resources are efficiently allocated when opening a connection to a file.


## Case Study

Wrangling and extracting meaningful information from a real-world dataset—the World Bank's World Development Indicators.

1. Welcome to the case study
2. Using python generators for streaming data
3. Using pandas' read_csv iterator for streaming data