# https://www.hackerrank.com/challenges/beautiful-binary-string/problem?
# isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def beautiful_binary_string(b):
    return b.count("010")


print(beautiful_binary_string("0101010"))
print(beautiful_binary_string("01100"))
print(beautiful_binary_string("0100101010"))
