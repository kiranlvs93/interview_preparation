# https://www.hackerrank.com/challenges/camelcase/problem

def camelcase(s):
    """
    The number of the letters in upper case is equal to the number of words
    Since the first word is in lower case, add one to the above count
    :param s:
    :return:
    """
    upper_case_letters = 0
    for ch in s:
        if ch.isupper():
            upper_case_letters += 1
    return upper_case_letters + 1


def camelcase_oneliner(s):
    return sum(map(str.isupper, s)) + 1


print("No of words is::", camelcase("saveChangesInTheEditor"))
print("No of words is::", camelcase_oneliner("saveChangesInTheEditor"))
