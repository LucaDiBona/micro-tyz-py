import Tokens.types_

heap = [{}]


def getVal(key:str):
    for i in reversed(heap):
        try:
            return(i[key.__str__()])
        except KeyError:
            pass
    raise KeyError("Variable not assigned")

def setVal(key:str,val):
    heap[-1][key.__str__()] = val

def enterBlock():
    heap.append({})

def exitBlock():
    if len(heap) < 1:
        raise KeyError("Can't break out of block")
    heap.pop()



