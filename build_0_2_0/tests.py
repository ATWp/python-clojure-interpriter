TESTS_CLOJURE = {
    'Input':[
        #тест на вывод данных в консоль
        {
            'test' : '(print 1)',
            'out': ['1'],
            'memmory':'',
        },
        {
            'test' : '(println 1)',
            'out': ['1'],
            'memmory':'',
        },
        {
            'test' : 'print(1)',
            'out': ['1'],
            'memmory':'',
        },
        {
            'test' : 'println(1)',
            'out': ['1'],
            'memmory':'',
        },
        {
            'test' : 'print (1)',
            'out': ['1'],
            'memmory':'',
        },
        {
            'test' : 'println (1)',
            'out': ['1'],
            'memmory':'',
        },
        {
            'test' : '(print "Hello, World!")',
            'out': ["Hello, World!"],
            'memmory':'',
        },
        {
            'test' : '(println "Hello, World!")',
            'out': ["Hello, World!"],
            'memmory':'',
        },
        {
            'test' : 'print("Hello, World!")',
            'out': ["Hello, World!"],
            'memmory':'',
        },
        {
            'test' : 'println("Hello, World!")',
            'out': ["Hello, World!"],
            'memmory':'',
        },
        {
            'test' : 'print ("Hello, World!")',
            'out': ["Hello, World!"],
            'memmory':'',
        },
        {
            'test' : 'println ("Hello, World!")',
            'out': ["Hello, World!"],
            'memmory':'',
        },
    ],
    
    'Const functions':[
        #тест на константные функции const function's
        {
            'test' : '(a 1)',
            'out': [],
            'memmory':'',
        },
    ],
    
    'Mathematics Operations':[
        #тест на математические операции
        {
            'test' : '(+ 1 1)',
            'out': ['2'],
            'memmory':'',
        },
        {
            'test' : '(- 1 1)',
            'out': ['0'],
            'memmory':'',
        },
        {
            'test' : '(* 1 1)',
            'out': ['1'],
            'memmory':'',
        },
        {
            'test' : '(/ 1 1)',
            'out': ['1.0'],
            'memmory':'',
        },
        {
            'test' : '(// 1 1)',
            'out': ['1'],
            'memmory':'',
        },
        {
            'test' : '(div 1 1)',
            'out': ['1'],
            'memmory':'',
        },
        {
            'test' : '(% 1 1)',
            'out': ['0'],
            'memmory':'',
        },
        {
            'test' : '(mod 1 1)',
            'out': ['0'],
            'memmory':'',
        },
    ],
    
    'sequential execution form':[
        #тест на последовательное выполнение множественных действий(форм-функций)
        {
            'test' : '''
                        (- 2 1)
                        (+ 3 1)
                       ''',
            'out': ['1','4'],
            'memmory':'',
        },
    ],
    
    'sequential execution with const form':[
        #тест на последовательное выполнение множественных действий(форм-функций)
        {
            'test' : '''
                        (a 1)
                        (+ a 1)
                       ''',
            'out': ['2'],
            'memmory':'',
        },
    ],
    
    'executing nested code':[
        #тест на выполнение вложенного кода
        {
            'test' : '''
                        (println 
                            (+ 1 1))
                       ''',
            'out': ['2'],
            'memmory':'',
        },
    ],
    
    'sequential execution nested form':[
        #тест на выполнение последовательного кода с вложенными form
        {
            'test' : '''
                        (a 1)
                        (println 
                            (+ a 1))
                       ''',
            'out': ['2'],
            'memmory':'',
        },
    ],
    
}