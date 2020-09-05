import re

pattern = r"(.+) \1"

if re.match(pattern, "abc abc abc"):
    print("match")

if re.match(pattern, "abc cde"):
    print("yes")


pattern1 = r"\D+\d"  # \d matches everything which is not a digit
# \ uppercase letters is opposite to lower case
if re.match(pattern1, "hi 87"):
    print("match")


pattern2 = r"\b(live)\b"  # \b matches the empty string
if re.search(pattern2, "i live in india"):
    print("match")


# email extraction
pattern3 = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

if re.search(pattern3, "please contact rochish@gmail.com for stuff"):
    print("match")
