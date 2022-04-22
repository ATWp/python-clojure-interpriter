from .functions import *


class Reserved_Functions():
    
    #reserved
    functions = {
            'print': print_args,
            'println': print_args,
            '__init__': init,
            '__write__': write,
            '__none__':  empty,
            '+': addition,
            '-': subtraction,
            '*': multiplication,
            '/': division,
            '//': integer_division,
            'div': integer_division,
            '%': remainder_of_division,
            'mod': remainder_of_division
    }
    
    def __init__(self):
        #reserved
        '''self.functions = {
                'print': self.print_args,
                'println': self.print_args,
                '__init__': self.init,
                '__write__': self.write,
                '__none__': self.none,
                '+': self.addition,
                '-': self.subtraction,
                '*': self.multiplication,
                '/': self.division,
                '//': self.integer_division,
                'div': self.integer_division,
                '%': self.remainder_of_division,
                'mod': self.remainder_of_division
        }'''
        pass
    
    def inReserved(self, function):
        if self.functions.get(function) == None:
            return False
        else:
            return True
    
    def function(self, function = '__none__', args = ['']):
        out = self.functions[function](args)
        print(out)
        return out