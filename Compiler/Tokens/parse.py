import Tokens.node as node


def parse(tokens: list):
    exprs = [token for token in tokens if token[1] != "WHITESPACE"]
    print(exprs)
    return(parseExpr(exprs))


def parseExpr(tokens: list):

    i = 0

    def curVal(i):
        return(tokens[i][0])

    def curCat(i):
        return(tokens[i][1])

    def nextVal(i):
        return(tokens[i+1][0])

    def nextCat(i):
        return(tokens[i+1][1])

    def funcLike(blockStyle: bool, i):

        name = curVal(i)

        argExprs = []
        curArg = []

        nesting = [1, 0]  # parens nesting, alt parens nesting
        if blockStyle:
            open_, close_ = "{", "}"
            altOpen, altClose = "(", ")"
            constructor_ = node.Block
        else:
            open_, close_ = "(", ")"
            altOpen, altClose = "{", "}"
            constructor_ = node.FunctionCall

        i += 2

        while True:

            cat = curCat(i)

            if nesting == [1,0]:

                if cat in ["STRING","NUMBER"]:
                    argExprs.append(parseExpr([tokens[i]]))

                elif cat == "ID":

                    if nextCat(i) == "SYMBOL":
                        nextChr = nextVal(i)
                        curArg.append(tokens[i])

                        if nextChr == close_:
                            argExprs.append(parseExpr(curArg))
                            break

                        curArg.append(tokens[i+1])
                        i += 1

                        if nextChr == open_:
                            nesting[0] += 1

                        elif nextChr == altOpen:
                            nesting[1] += 1


                        else:
                            pass #TODO error

                    else:
                        argExprs.append(parseExpr([tokens[i]]))

                elif curVal(i) == close_:
                    if curArg:
                        argExprs.append(parseExpr(curArg))
                    break

                else:
                    pass #TODO error


            else:
                curArg.append(tokens[i])

            if cat == "SYMBOL" and nesting != [1,0]:

                curChr = curVal(i)

                if curChr == close_:
                    nesting[0] -= 1
                    if nesting == [0,0]:
                        argExprs.append(parseExpr(curArg))
                        break

                    elif nesting == [1,0]:
                        argExprs.append(parseExpr(curArg))
                        curArg = []

                    elif nesting[0] == 0:
                        pass #TODO error

                elif curChr == open_:
                    nesting[0] += 1

                elif curChr == altClose:
                    nesting[1] -= 1
                    if nesting == [1,0]:
                        argExprs.append(parseExpr(curArg))
                        curArg = []
                    elif nesting[1] < 0:
                        pass #TODO error


                elif curChr == altOpen:
                    nesting[1] += 1

            i += 1

        return(constructor_(name,argExprs),i)


    while i < len(tokens):

        if curCat(i) == "ID":

            if len(tokens) > 1 and nextCat(i) == "SYMBOL":

                if nextVal(i) == "(":
                    obj, i = funcLike(False, i)
                    return(obj)

                elif nextVal(i) == "{":
                    obj, i = funcLike(True, i)
                    return(obj)

            else:
                return(node.Variable(curVal(i)))

        elif curCat(i) == "STRING":
            return(node.StringLiteral(curVal(i)))

        elif curCat(i) == "NUMBER":
            return(node.IntLiteral(curVal(i)))

        i += 1
