stuff = ["a","ab","abc","abcd","abcde"]

def isIn(str):
    return str in ["a", "b", "c"]

for x in stuff:
    print(all(isIn(i) for i in x))

print("0132e0"[-2:])
print("abc"[:2])