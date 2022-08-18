def singleChar(check):
    def wrapper(char:chr):
        if len(char) != 1:
            raise(NameError("Must be a single character"))
        return(check(char))
    return(wrapper)

@singleChar
def isAorU(char:chr):
    return(char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_")

@singleChar
def isNum(char:chr):
    return(char in "0123456789")

@singleChar
def isWs(char:chr):
    return(char in " \t\n\r\v")

def isSym(char:chr):
    return(not(isAorU(char) or isNum(char) or isWs(char)))

def isID(string:str):
    return all(isAorU(i) or isNum(i) for i in string[1:]) if isAorU(string[0]) else False

def isNumber(string:str):
    return all(isNum(i) for i in string)

def isWsBlock(string:str):
    return all(isWs(i) for i in string)

def pretokenise(text):
    def charType(char:str):
        if isWs(char):
            return(isWsBlock,"WHITESPACE")
        elif isAorU(char):
            return(isID,"ID")
        elif isNum(char):
            return(isNumber,"NUMBER")
        else:
            return("SYMBOL") #symbolic - but each symbol should be parsed separately


    textPos = 0
    text += " "
    targetLength = len(text)
    chunks = []

    def scan(args):

        rule = args[0]
        name = args[1]

        nonlocal textPos
        currentStr = text[textPos]

        while textPos < targetLength and rule(currentStr):

            textPos += 1
            try:
                currentStr += text[textPos]
            except IndexError:
                return("","EOF")

        currentStr = currentStr[:-1]
        return(currentStr,name)


    def MaxMunch(str:str):
        pass


    while textPos < targetLength:

        currentChr = text[textPos]
        curCharType = charType(currentChr)
        if curCharType == "SYMBOL":
            chunks.append((currentChr,"SYMBOL"))
            textPos += 1
        else:
            chunks.append(scan(curCharType))

    return(chunks)


    #TODO string parsing
    #TODO other numbers parsing



def getLiterals(chunks):

    #TODO replace tuple with object, generate value


    def isUNumerical(string):
        #finds strings of the form _000_00
        if string[0] != "_":
            return False
        return all((i == "_" or isNum(i)) for i in string)

    def boxAllowed(integer:str):
        length = len(integer)
        if length == 0:
            return False
        elif length == 1:
            return (integer == "0")
        elif length == 2:
            return False
        else:
            return (integer[-2:] == "e0" or integer[-3:] in ["eb0","eo0","ex0"])

    def isExp(integer:str):
        length = len(integer)
        if length < 2:
            return False
        else:
            return (i[0][0] == "e" or i[0][:2] in ["eb","eo","ex"])




    #~~~~~STRINGS

    inStr = False
    curStr = ""
    newChunks = []

    for i in chunks:
        if i[0] == "`":
            if inStr:
                inStr = False
                newChunks.append((curStr,"STRING"))
                curStr = ""
            else:
                inStr = True
        elif inStr:
            curStr += i[0]
        else:
            newChunks.append(i)

    #~~~~INTS

    #first phase - underscores

    chunks = newChunks
    inInt = False
    curInt = ""
    newChunks = []

    for i in chunks:
        if i[1] == "NUMBER":
            inInt = True
            curInt += i[0]
        elif inInt:
            if i[1] == "ID" and isUNumerical(i[0]):
                curInt += i[0]
            else:
                newChunks.append((curInt,"NUMBER"))
                curInt = ""
                inInt = False
                newChunks.append(i)
        else:
            newChunks.append(i)

    #second phase - letters

    chunks = newChunks
    inNum = False
    curNum = ""
    hasExp = False
    newChunks = []

    for i in chunks: #note this does not handle decimal points as these are a macro - this means that 1..10 can be defined
        if i[1] == "NUMBER":
            inNum = True
            curNum += i[0]
        elif inNum:
            if i[0] == "-":
                if curInt[-1] in "ebox":
                    curNum += "-"
                else:
                    newChunks.append((curNum,"NUMBER"))
                    inNum = False
                    hasExp = False
                    curNum = ""
                    newChunks.append(i)
            elif boxAllowed(curNum):
                if i[0][0] in ["b","o","x"]:
                    curNum += i[0]
                else:
                    newChunks.append((curNum,"NUMBER"))
                    inNum = False
                    hasExp = False
                    curNum = ""
                    newChunks.append(i)
            elif not hasExp and isExp(i[0]):
                curNum += i[0]
            else:
                newChunks.append((curNum,"NUMBER"))
                inNum = False
                hasExp = False
                curNum = ""
                newChunks.append(i)
        else:
            newChunks.append(i)

    #TODO proper hex support


    #no specials, they are defined with atom constructors - eg macro Null -> __atom__(`Null`)

    return(newChunks)



def tokenise(text:str):
    chunks = pretokenise(text)
    chunks = getLiterals(chunks)
    return(chunks)



#TODO x!! is equivalent to x = !x

#TODO rewrite this to simplify - only handle basic cases and only allow a few symbols