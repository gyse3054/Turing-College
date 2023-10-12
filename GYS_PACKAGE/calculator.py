"""
This module contains a calculator implementation.
"""
__version__ = '1.0.0'

class Calculator:
    def __init__(self):
        '''
        Initialize the calculator with a base value of 0.
        '''
        self.value = 0
    
    def add(self, argument: float):
        '''
        Base value is summed with the provided argument.

        :param argument: The value that will be added
        :type argument: float

        :return: The updated base value.
        :rtype: float
        '''
        self.value += argument
        return self.value
    
    def subtract(self, argument: float):
        '''
        Base value is substracted from the provided argument.

        :param argument: The value to be subtracted.
        :type argument: float
        
        :return: The updated base value.
        :rtype: float
        '''
        self.value -= argument
        return self.value

    def multiply(self, argument: float):
        '''
        Base value is multiplied by the provided argument.

        :param argument: The value to multiply by.
        :type argument: float
        
        :return: The updated base value.
        :rtype: float
        '''
        self.value *= argument
        return self.value
    
    def divide(self, argument: float):
        '''
        Base value is divided from the provided argument. 

        :param argument: The value to divide by.
        :type argument: float
        
        :raises ValueError: If the argument is 0.
        
        :return: The updated base value.
        :rtype: float
        '''
        if argument == 0:
            raise ValueError("0 can't be processed. Please pick another number")
        else:
            self.value /= argument
        return self.value

    def take_root(self, x: float):
        '''
        X root is taken from the argument.  

        :param x: The root to be taken.
        :type x: float
        
        :raises ValueError: If the base value is negative and x is even.
        
        :return: The result of the root operation.
        :rtype: float
        '''
        if self.value < 0 and x % 2 == 0:
            raise ValueError("Can only take odd root of a negative number")
        else: 
            self.value **= (1/x)
        return self.value
    
    def reset_memory(self):
        '''
        Reset the base value to zero.
        '''
        self.value = 0


