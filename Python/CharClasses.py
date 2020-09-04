import re

pattern = r"[aeiou]"

if re.search(pattern, "this is all"):
    print("match")


pattern1 = r"[^A-Z]"

if re.search(pattern1, "this is rochish"):
    print("match")

if re.search(pattern1, "THIGFBKKGK"):  # doesnt consider
    print("yeah")
