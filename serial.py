"""Python serial number generator."""
import doctest
class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        ''' 
        initializes self
        has a start number 
        '''
        self.start = start
        self.og = start
    
    def generate(self):
         '''
         evertime generate method is used, increment by 1
         subtract by one so when you first start generating you start at your number 
          '''
         self.start += 1
         return self.start - 1 
         
    
    def reset(self):
     '''
     set the start back to og number, so when genertating you start back at the number you orgininally put in 
       '''
     self.start = self.og
     return 

