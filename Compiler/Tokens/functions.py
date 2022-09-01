import Tokens.heap as heap

class Func():

    def __init__(self,name:str,args:list):
        self.name = name
        self.args = args

    def eval_(self):
        raise(NotImplementedError)

class Param():

    def __init__(self):
        pass

class NamedParam(Param):
    pass

class OptParam(Param):
    pass

class OptNamedParam(Param):
    pass

class ListParam(Param):
    pass
class OptListParam(Param):
    pass

class Params():

    def __init__(self,):
        pass

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

def func_():
    pass

def list_():
    pass


BUILTINS = {
    "__print__": Builtin("__print__",["str"],print_),
    "__add__": Builtin("__add__",["leftInt","rightInt"],add_),
    "__assign__":Builtin("__assign__",["name","val"],assign_),
    "__func__":Builtin("__func__",[],func_),
    "__list__":Builtin("__list__",[],list_)
}


BUILTINS["__print__"].eval_(["test"])
x=BUILTINS["__add__"].eval_([2,3])
BUILTINS["__print__"].eval_([x])