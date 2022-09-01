import sys
from Tokens.tokeniser import tokenise
from Tokens.parse import parse

print(sys.path[0])
f = open("Compiler/helloWorld.mnt")
def main(args:list):

    if not args:
        print("No file provided")
        sys.exit(1)

    with open(args[0]) as f:
        text = f.read()

    x = parse(tokenise(text))
    print(x.print_())
    x.eval_()


if __name__ == "__main__":
    main(["Compiler/helloWorld.mnt"])
    ##main(sys.argv[1:])