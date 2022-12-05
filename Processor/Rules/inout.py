import var
from collections.abc import Sequence

class InOut(Sequence):

    def __init__(self,contents: list[var.Placeholder|str]):
        for i in contents:
            if not (isinstance(i, (str, var.Placeholder))):
                raise ValueError("Rule must contain only strs and vars")

        self.contents = contents
        self._index = 0

    def __getitem__(self, i:int):
        return(self.contents[i])

    def __len__(self):
        return(len(self.contents))

    def getVars(self):
        return([x for x in self.contents if isinstance(x,var.Placeholder)])
