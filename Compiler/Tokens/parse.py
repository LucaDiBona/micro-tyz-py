import Tokens.node as node

def parse(tokens:list):
    return(parseExpr(tokens))

def parseExpr(tokens:list):

    i = 0


    def curVal():
        return(tokens[i][0])

    def curCat():
        return(tokens[i][1])

    def nextVal():
        return(tokens[i+1][0])

    def nextCat():
        return(tokens[i+1][1])

    while i < len(tokens):

        if curCat() == "ID":

            if nextCat() == "SYMBOL" and nextVal() == "(":

                #function call parsing

                funcName = curVal()

                argExprs = []
                curArgTokens = []
                nesting = 1

                i+= 2
                while nesting > 0:
                    if curCat() == "SYMBOL":
                        if curVal() == "(":
                            nesting += 1
                        elif curVal() == ")":
                            nesting -= 1
                            if nesting == 0:
                                break
                        elif nesting == 1 and curVal() == ",":

                            #if current arg non empty, append parsed arg
                            if curArgTokens != []:
                                argExprs.append(parseExpr(curArgTokens))
                                curArgTokens = []
                            i+=1
                            continue

                    curArgTokens.append(tokens[i])
                    i+=1
                curArgTokens.append(("EOE","EOE")) # end of expression
                argExprs.append(parseExpr(curArgTokens))

                return(node.FunctionCall(funcName,argExprs))






            else:

                return(node.Variable(curVal()))

        elif curCat() == "STRING":
            return(node.StringLiteral(curVal()))

        elif curCat() == "NUMBER":
            return(node.IntLiteral(curVal()))



        print(i)
        print(tokens[i])

        i += 1


