from inout import InOut
import var

class Rule():

    def __init__(self,rule: InOut,out: InOut,prec: int):
        self.rule = rule
        self.out = out
        self.prec = prec
        self.vars = [x.toVar() for x in rule.getVars()]

    def replace(self,input: InOut):
        #assign values to vars
        for i,val in enumerate(self.rule):
            if isinstance(val,var.Placeholder):
                for j in self.vars:
                    if j.name == val.name:
                        j.setVal(input[i])

        #replacement logic
        def getReplacement(x:var.Placeholder|str):
            if isinstance(x, str):
                return(x)

            for i in self.vars:
                if i.name == x.name:
                    return(i.getVal())

            raise ValueError("Variable not found")

        if len(input) != len(self.rule):
            raise ValueError("Length of input different from length of rule")

        return([getReplacement(x) for x in self.out])

assign = Rule(InOut([var.Placeholder("left"), "=", var.Placeholder("right")]),InOut(["__assign__(`",var.Placeholder("left"),"` ",var.Placeholder("right"),")"]),100)

out=assign.replace(["a[0]","=","rect(x,y)"])
print(out)