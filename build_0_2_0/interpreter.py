from .parse_code import normal_split
from .reserved_functions import Reserved_Functions


class CLython:
    
    # Memmory and Call reserved functions
    output = []
    
    memmory = {}
    functions = {}
    '''functions = {
        'reserved':{
            'print':print_args,
            'println':print_args,
            '__init__':init,
            '__write__':write,
            '__none__':none,
            '+': addition,
            '-': subtraction,
            '*': multiplication,
            '/': division,
            '//': integer_division,
            'div': integer_division,
            '%': remainder_of_division,
            'mod': remainder_of_division
        }
    }'''
    
    def __init__(self, thread = 'main', code = ''):
        self.output = []
        if code == '':
            print(f'Error: Код пустой!')
            
        else:
            #записываем код
            self.code = code
            self.reserved = Reserved_Functions()
            #создаем пустой поток main
            self.functions['main'] = {} #{'__init__':init,}
            self.thread = 'main'
            self.clython()
    
    
    def parser(self):
        sep = {
            'all': ' ()',
            'delete': ' ',
            'not-delete': '()'
        }
        parse_code = normal_split(self.code, sep)
        print(f'parse_code: {parse_code}')
        return parse_code

    def command_doings(self):
        print(f'parse_code: {self.parse_code}')
        parse_code = self.parse_code
        
        command_doing = []
        length = len(parse_code)
        num = 0
        #создание потока main
        #наследование базовых функций?

        while length >= num:
            doing = parse_code[num]

            if doing == '(':
                # Данная функция находится в reserved
                name_func = parse_code[num+1]
                args = parse_code[num+2:-1]
                if self.reserved.inReserved(name_func):
                    command_doing.append(
                        {
                            'function': parse_code[num+1],
                            'type': '__magic__',
                            'args': parse_code[num+2:-1]
                        }) 
                else:
                    command_doing.append(
                        {
                            'function': '__init__',
                            'type': '__magic__',
                            'args': parse_code[num+1]
                        })
                    command_doing.append(
                        {
                            'function': '__write__',
                            'type': '__magic__',
                            'args': [parse_code[num+1], parse_code[num+2:-1]]
                        })

                num = length+1
                #удаление значения и функции?
            else:
                num = length+1
                print(f'Ошибка синтаксиса: Не найдена скобка вначале строки!')
        
        print(f'command_doings: {command_doing}')
        return command_doing        

    def interpreter(self):
        print(f'command_doings: {self.command_doing}')
        for command in self.command_doing:
            print(f'command: {command}')
            if command['type'] == '__magic__':
                out = self.reserved.function(command['function'], command['args'])
                
            elif command['type'] == '__normal__':
                out = self.functions[self.thread][command['function']](command['args'])
            
            #print(out)
            if out != None:
                self.output.append(str(out))
            
    def clython(self):
        print(self.code)
        self.parse_code = self.parser()
        self.command_doing = self.command_doings()
        self.interpreter();
        
        print(f'output: {self.output}')
        #print(f'functions: {self.functions}')
        print('Выполнение кода завершено!')