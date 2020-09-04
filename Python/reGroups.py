import re

pattern = r"raptor(treats)*"

if re.match(pattern, "raptor"):
    print("match")

if re.match(pattern, "raptortreatstreatsraptor"):
    print("match")

if re.match(pattern, "treats"):
    print("haha")


pattern1 = r"a(bc)(de)(f(g)h)i"

matc = re.match(pattern1, "abcdefghi")

if matc:
    print(matc.group(2))
    print(matc.groups())
