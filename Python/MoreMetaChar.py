import re

pattern = r"raptor(treats)*"  # * means zero or more reps of prev thing

if re.match(pattern, "raptor"):
    print("match")

if re.match(pattern, "raptortreatstreatsraptor"):
    print("match")

if re.match(pattern, "treats"):
    print("haha")


pattern1 = r"g+"  # one or more characters

if re.match(pattern1, "gggggggggg"):
    print("matchhhhh")


pattern2 = r"raptor(-)?treats"  # zero or one reps

if re.match(pattern2, "raptor-treats"):
    print("ooooo yeah")

if re.match(pattern2, "raptor--treats"):
    print("samuel")


pattern4 = r"2{1,3}$"  # number of reps between two numbers

if re.match(pattern4, "222"):
    print("u go")

if re.match(pattern4, "2222"):
    print("yes")
