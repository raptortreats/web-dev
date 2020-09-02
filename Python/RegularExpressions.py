# importing the regular expressions library

import re

str = "superman can kick batman's ass but can be outsmart by him aswell"

pattern = r"superman"

# checks whether the pattern is in the string or no
if re.match(pattern, str):
    print("yeah")
else:
    print("nope")

# similarly we have RE.SEARCH which finds the match of pattern anywhere in the string

print(re.findall(pattern, str))

# similarly we have
match = re.search(pattern, str)
print(match.group())
print(match.start())
print(match.end())
print(match.span())  # returns a tuple containing start and end indexes of pattern

# to replace
newstr = re.sub(pattern, "wonderwoman", str)
print(newstr)
