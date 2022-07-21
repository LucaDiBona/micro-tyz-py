import functions,heap,types_

class Node():

    def __init__(self,name:str):
        self.name=name

    def eval_(self):
        raise(NotImplementedError)

class Literal(Node):

    def __init__(self,name:str):
        super().__init__(name)

class StringLiteral(Literal):

    def __init__(self,val:str):
        super().__init__(val)

    def eval_(self):
        return(types_.Str_(self.name))

class IntLiteral(Literal):

    def __init__(self,val:str):
        super().__init__(val)

    def eval_(self):
        return(types_.Int_(self.name))

class Lambda(Literal):

    def __init__(self, name: str):
        super().__init__(name)

class FunctionCall(Node):

    def __init__(self,name:str,args:list):
        self.args = args
        super().__init__(name)

    def eval_(self):
        #check if builtin

        #print(self.args)

        argVals = [i.eval_() for i in self.args]

        if self.name in functions.BUILTINS:
            return(functions.BUILTINS[self.name].eval_(argVals))

        # lookup value

class Variable(Node):

    def __init__(self,name:str):
        super().__init__(name)

    def eval_(self):
        return(heap.getVal(self.name))

class Block(Node):

    def __init__(self,contents:list[Node]):
        self.end = contents.pop()
        self.contents = contents
        super().__init__("Block")

    def eval_(self):
        heap.enterBlock()
        [i.eval_() for i in self.contents]
        retVal = self.end.eval_()
        heap.exitBlock()
        return(retVal)

"""
w=FunctionCall("__assign__",[StringLiteral("test"),IntLiteral("0")])
w.eval_()
test=Variable("test")
print(heap.heap)
print(test.eval_())

x =FunctionCall("__assign__",[StringLiteral("x"),test])
x.eval_()
h = heap.heap
print(heap.heap) """


#TODO allow functions as first class objects - assigning them
#TODO allow assigning to a variable

y = Block([FunctionCall("__print__",[StringLiteral("test")]),FunctionCall("__add__",[IntLiteral("2"),IntLiteral("2")])])
print(y.eval_())