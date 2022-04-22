

def print_args(*args):
    #global output
    
    print(type(args))
    print(args)
    
    new_args = []
    for arg in args:
        if type(arg) == type(list()):
            new_args.append(' '.join(arg))
        else:
            new_args.append(str(arg))
    out = ' '.join(new_args)
    #output.append(' '.join(new_args))        
    print(f'print_args: '+ out)
    return out
	
def empty(*args):
    out = args
    return out
	
def init(args):   
    thread = 'main'
    if functions['reserved'].get(args) != None:
        functions[thread][args] = functions['reserved'][args]
        
    elif functions['reserved'].get(args) == None:
        functions[thread][args] = functions['reserved']['__none__']
		
def write(args):   
    thread = 'main'
    func_name = args[0]
    args = args[1]
    print(f'func_name: {func_name}')
    print(f'args: {args}')
    functions[thread][func_name] = functions[thread][func_name](args) 
	
def assignment(args):
    return ''
	
def addition(args):
    sum_ = sum([int(arg) for arg in args])
    return sum_
	
def subtraction(args):
    sub_ = int(args[0])
    for arg in args[1:]:
        print(arg)
        sub_ -= int(arg)
    return sub_
	
def multiplication(args):
    mult_ = 1
    for arg in args:
        mult_ *= int(arg)
    return mult_
	
def division(args):
    div_ = int(args[0])
    for arg in args[1:]:
        div_ /= int(arg)
    return div_
	
def integer_division(args):
    idiv_ = int(args[0])
    for arg in args[1:]:
        idiv_ //= int(arg)
    return idiv_
	
def remainder_of_division(args):
    mod_ = int(args[0])
    for arg in args[1:]:
        mod_ %= int(arg)
    return mod_
	
