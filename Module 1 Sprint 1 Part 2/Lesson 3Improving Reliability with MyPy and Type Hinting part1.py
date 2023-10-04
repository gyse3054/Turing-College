from typing import *
from collections import OrderedDict, Deque, namedtuple
import secrets

x = 10                  # type: int  ##we can anotate like this



x: int = 10 #mypy can't handle this


def f(x: int,y: int) -> int: #we can anotate like this
    return  x + y # can add strings and numbers

y = OrderedDict()       #type: OrderedDict

def g(x: Sequence) -> None:
    print(len(x))
    print(x[2])
    for i in x:
        print(i)
    print()

#Mypy can help find type errors before running code.

person = ('Gytis', 5*2 +11)     #type: Tuple[str, float]
lol = ('Gytis', 'Gytis', 'Gytis', 'Gytis', 'Gytis')     #type: Tuple[str, ...]

def f(x: int,y: Optional(int) = None) -> int: 
    if y is None:
        y = 20
    return  x + y 

a = Deque()         #type: Deque

Point = NamedTuple('Point', [('x', int) ,('y', int)])

#To test your code write: python -m mypy test.py
#To test your code write: python -m pyflakes test.py
#To test your code write: python -m hypothesis test.py
#To test your code write: python -m unittest test.py  #unittest -> nose py.test

    #Mypy is a static type checker for ensuring type safety and correctness in your code.
    #Pyflakes is a static code analysis tool for detecting basic code correctness issues.
    #Hypothesis is a property-based testing library that automates test case generation based on defined properties.
    #Unittest is Python's built-in testing framework for writing and organizing unit tests.
