import sys
print(sys.path)
def main(args:list):

    if not args:
        print("No file provided")
        sys.exit(1)

    with open(args[0]) as src:
        src_text = src.read()

    with open(args[2]) as rules:
        rules_text = rules.read()

    #out = process(src,parseRules(rules_text))
    out = "test"

    with open(args[1],"w") as target:
        target.write(out)

if __name__ == "__main__":
    main(["Processor/in.tyz","out.mnt","Processor/rules"])
    ## main(sys.argv[1:])