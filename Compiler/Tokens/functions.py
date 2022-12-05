import Tokens.heap as heap


class Func():

    def getArgs():
        pass

    def __init__(self, name: str, args: list):
        self.name = name
        self.args = args

    def eval_(self):
        raise(NotImplementedError)


class Param():

    def __init__(self, name: str):
        self.name = name


class OptParam(Param):

    def __init__(self, name: str, default):
        self.default = default
        super().__init__(name)


class ListParam(Param):

    def __init__(self):
        super().__init__(".list")


class Params():

    def __init__(self, params: list[str], optParams: list[tuple[str, str]], hasMore: bool, moreName: str | None = None):
        self.params = [Param(param) for param in params]
        self.optParams = [OptParam(param) for param in optParams]
        self.hasMore = hasMore
        self.moreName = moreName

    @staticmethod
    def fromList(params: list[str]):
        return(Params(params, [], False))

# __param__(`name`)
# __optParam__(`name`,`value`)
# __func__(__tuple__(`name` __tuple__(`name`,`value`) __tuple__(`name`))))
# __func__(__tuple__(`param1` `param2`) __tuple__(__tuple(`param3` `value`)) `name`)


class Builtin(Func):

    def __init__(self, name: str, params: list, func):
        self.func = func
        super().__init__(name, params)

    def eval_(self, inputs):
        return(self.func(*inputs))


def print_(string):
    print(string)


def add_(leftInt, rightInt):
    return(leftInt + rightInt)


def assign_(name, val):
    heap.setVal(name, val)


def func_(*params):

    #detect if vargs present
    if len(params) == 3:
        hasMore = True
        moreName = params[2] #TODO update this to be accurate

    else:
        hasMore = False
        moreName = None

    #TODO unpack tuples ig?





def list_():
    pass

def tuple_():
    pass

BUILTINS = {
    "__print__": Builtin("__print__", Params.fromList(["str"]), print_),
    "__add__": Builtin("__add__", Params.fromList(["leftInt", "rightInt"]), add_),
    "__assign__": Builtin("__assign__", Params.fromList(["name", "val"]), assign_),
    "__func__": Builtin("__func__", Params([],[],True,"params"), func_),
    "__list__": Builtin("__list__", Params([],[],True,"vals"), list_),
    "__tuple__": Builtin("__tuple__", Params([],[],True,"vals"), tuple_)
}


BUILTINS["__print__"].eval_(["test"])
x = BUILTINS["__add__"].eval_([2, 3])
BUILTINS["__print__"].eval_([x])
