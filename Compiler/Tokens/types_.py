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

class Str_(Type_):

    def __init__(self,val:str):
        self.val = val

    def __str__(self):
        return(self.val)
