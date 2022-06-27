def pretokenise(text):

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

    def isUnderscores(string):
        return(all(i == "_" for i in string))

    #~~~~~STRINGS

    inStr = False
    curStr = ""
    newChunks = []

    for i in chunks:
        if i[0] == "`":
            if inStr:
                inStr = False
                newChunks.append((curStr,"STRING"))
            else:
                inStr = True
        elif inStr:
            curStr += i[0]
        else:
            newChunks.append(i)

    #~~~~INTS

    #first phase - underscores

    for i in chunks:
        if i[1] == "NUMBER"

    #~~~~FLOATS

    pass

    #~~~~SPECIAL

    pass

    return(newChunks)



def tokenise(text:str):
    chunks = pretokenise(text)
    chunks = getLiterals(chunks)
    return(chunks)


print(tokenise("__print__(hello world)"))
print(tokenise("__print__(`hello world`)"))

#TODO x!! is equivalent to x = !x