import heap

class Func():

    def __init__(self,name:str,args:list):
        self.name = name
        self.args = args

    def eval_(self):
        raise(NotImplementedError)

class Builtin(Func):

    def __init__(self,name:str,argNames:list,func):
        self.name = name
        self.argNames = argNames
        self.func = func

    def eval_(self,inputs):
        return(self.func(*inputs))

def print_(string):
    print(string)

def add_(leftInt,rightInt):
    return(leftInt + rightInt)

def assign_(name,val):
    heap.setVal(name,val)

BUILTINS = {
    "__print__": Builtin("__print__",["str"],print_),
    "__add__": Builtin("__add__",["leftInt","rightInt"],add_),
    "__assign__":Builtin("__assign__",["name","val"],assign_)
}


BUILTINS["__print__"].eval_(["test"])
x=BUILTINS["__add__"].eval_([2,3])
BUILTINS["__print__"].eval_([x])