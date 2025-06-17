# DSA using Python 

## Arrays and List

 **Array** is a collection of similar type of elements 
- Array's size is fixed 
- Indexed 

 **Dynamic Array** is a collection of similar type of elements 
- Array's size is resizable 
- Indexed 

### Array Module
**Array** is not a **built-in** *data structure* and therefore need to be imported.

*Arrays* are sequence types and behave very much like **Lists** , but __Arrays__ can have elements of __limited types__.

### Creating an Array

```python
from array import *
a1 = array('i', [23, 45, 56,25])
for x in a1:
    print(x)
```

### Type codes

### Array methods
#### append()
```python 
a1.append(2)
```
#### count()
```python 
a1.count(45)
```
#### extend()
```python 
a1.append(2)
```
#### fromlist()
#### index()
```python 
a1.index(25)
```
#### insert()
#### pop()
```python 
a1.pop()
```
#### remove()
#### reverse()
#### tolist()

### List
_List_ is a __class__
_List_ is __mutable__
_List_ elements are __indexed__
_List_ is an __iterable__
_List_ can grow (dynamic array)
_List_ can contain __different type__ of elements

### Creating List Object

```python
l1 = [10, 20, 30, 40, 50]
l2 = []
l3 = [10, 3.14, 'hello', True]
```

### methods of List

len()

sum()

max()

min()

sorted()

### Numpy Intro

If you want to perform mathematical calc , then you should use Numpy arrays by importing Numpy package.

Otherwise use __lists__ as it works in a similar way and more flexible to work with.

__Install Numpy__

```bash
> pip install numpy
```

```python

import numpy as np
a = np.array([1,2,3,4])
print(a)
b = np.array([[1,2,3,4],[10,20,30,40]]) #2D array
print(b)
c = np.array([[1,2,3],[10,20]]) #1D array with two list type elements
print(c)

```
----------

## Class



## Attributes

## Objects

## Class Object

## __init__() object

## Types of methods

## Types of variables

