# You are given a string containing characters  and  only.
# Your task is to change it into a string such that there are no matching adjacent characters.
# To do this, you are allowed to delete zero or more characters in the string.
# Your task is to find the minimum number of required deletions.

def alternating_characters(s):
    print(f"Checking for string inp {s}")
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
    return count


inputs = ["AAAA", "BBBBB", "ABABABAB", "BABABA", "AAABBB"]
for inp in inputs:
    print("Minimum number of required deletions are ->", alternating_characters(inp))
    print("************************")
