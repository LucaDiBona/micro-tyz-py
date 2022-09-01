class Type_():

    def __init__(self):
        self.val = None

    def eval_(self):
        return(self.val)

class Int_(Type_):

    def __init__(self,val:str):
        self.val = int(val)

    def __add__(self,val2):
        return(Int_(self.val + val2.val))

    def __str__(self):
        return(str(self.val))

class Null_(Type_):

    def __init__(self):
        self.val = None

class Str_(Type_):

    def __init__(self,val:str):
        self.val = val

    def __str__(self):
        return(self.val)

class Function_(Type_):

    def __init__(self,val):
        self.val = val

    def call_(self,args:list):
        self.val.call_(args)

class List_(Type_):

    def __init__(self,val:list) ->None:
        self.val = val

    def __str__(self):
        return(str(self.val))

    def getVal_(self,i:int):
        return(self.val[i])

    def setVal_(self,i:int,newVal):
        self.val[i] = newVal