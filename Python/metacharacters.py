import re

pattern = r"w.ng"

if re.match(pattern, "wing"):
    print("yes")

if re.match(pattern, "wong"):
    print("yo")

if re.match(pattern, "bong"):
    print("r u kiddin")


# matching start and end of the string

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("matched")
