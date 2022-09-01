import Tokens.functions as functions
import Tokens.heap as heap
import Tokens.types_ as types_

nesting = 0

class Node():

    def __init__(self,name:str):
        self.name=name

    def eval_(self):
        raise(NotImplementedError)

    def print_(self):
        raise(NotImplementedError)

class Block(Node):

    def __init__(self,blockName:str,contents:list[Node]):
        self.isScope = (blockName == "__blockScope__") #mess about with this if we want more than two kinds of block
        if contents:
            self.end = contents.pop()
        else:
            self.end = NullLiteral()
        self.contents = contents
        super().__init__("Block")

    def inject(self,expr:Node,pos:int):
        #injects an expr in the block
        self.contents.insert(pos,expr)

    def eval_(self):
        if self.isScope:
            heap.enterBlock()
        [i.eval_() for i in self.contents]
        retVal = self.end.eval_()
        if self.isScope:
            heap.exitBlock()
        return(retVal)


    def print_(self):
        retStr = "Block: {\n"
        for i in self.contents:
            retStr += "    "
            retStr += i.print_()
            retStr += "\n"
        retStr += self.end.print_()
        retStr += "\n}"
        return(retStr)

class Literal(Node):

    def __init__(self,name:str):
        super().__init__(name)

    def print_(self):
        return("Literal: " + self.name)

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

class NullLiteral(Literal): #actually __block__{}

    def __init__(self):
        super().__init__("Null")

    def eval_(self):
        return(types_.Null_())


class Lambda(Literal):

    def __init__(self, params:list[str], contents:Block):
        self.params = params
        self.contents = contents
        super().__init__("lambda")

    def eval_(self):
        return(types_.Function_(self))

    def call_(self,args:list[types_.Type_]):
        argPairs = zip(self.params,args,strict=True)
        for i in argPairs:
            self.contents.inject(FunctionCall("__assign__",[i[0],i[1]]),0)
        self.contents.eval_()

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
        return(Variable(self.name).eval_().call_(argVals))

    def print_(self):
        retStr = "Function Call: " + self.name + "{\n"
        print(self.args)#why is this sometimes [None] not just []
        for i in self.args:
            retStr += "    "
            retStr += i.print_()
            retStr += "\n"
        retStr += "}"
        return(retStr)


class Variable(Node):

    def __init__(self,name:str):
        super().__init__(name)

    def eval_(self):
        return(heap.getVal(self.name))

    def print_(self):
        return("Variable: " + self.name)


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

#y = Block([FunctionCall("__print__",[StringLiteral("test")]),FunctionCall("__add__",[IntLiteral("2"),IntLiteral("2")])])
#print(y.eval_())
"""

x = FunctionCall("__assign__",[StringLiteral("x"),StringLiteral("Hello, world!")])
x.eval_()
y = FunctionCall("__print__",[Variable("x")])
y.eval_()


 """




