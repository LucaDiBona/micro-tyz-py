class Var():

    def __init__(self,name:str):
        self.name = name
        self._val = None

    def setVal(self,val):
        self._val = val

    def getVal(self):
        if not self._val:
            raise ValueError("Variable has no value")

        else:
            return(self._val)

class Placeholder():

    def __init__(self,name:str):
        self.name = name

    def toVar(self):
        return(Var(self.name))