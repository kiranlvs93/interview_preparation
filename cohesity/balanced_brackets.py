# https://www.hackerrank.com/challenges/balanced-brackets/problem
# https://www.youtube.com/watch?v=WTzjTskDFMg

def validate_brackets(inp: str):
    """
    :param inp:
    :return: 
    """
    # Stack/list to keep track of the brackets  
    stack = []

    # Dictionary for matching the closing brackets with open brackets
    close_to_open = {"}": "{", "]": "[", ")": "("}

    # If the no of characters aren't even or 0 then its invalid
    if len(inp) % 2 != 0 or len(inp) == 0:
        return False
    else:
        for ch in inp:
            # For closing braces
            if ch in close_to_open.keys():
                # If the stack isn't empty and the current bracket is equal to its matching open bracket
                # Pop the current open bracket from the list
                # If the current closing bracket doesn't match with its corresponding open bracket return False
                if stack and stack[-1] == close_to_open[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        # At the end of the operations, stack should be empty
        return True if not stack else False


if __name__ == '__main__':
    brackets = ["{{[[(())]]}}", "{[()]}", "{[(])}", ")(", ""]
    for bracket in brackets:
        print(f"{bracket}->{validate_brackets(bracket)}")
