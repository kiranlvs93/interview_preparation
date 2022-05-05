def longest_unique_substr(inp):
    """
    Getting longest sub-string without non-repeating characters
    :param inp:
    :return:
    """
    max_length = 0
    sub_str_list = []

    for i in range(len(inp)):
        sub_str = ""
        visited = set()
        for j, ch in enumerate(inp[i:]):
            # If the character is not visited, increase the length of the sub-string and add to visited set
            if ch not in visited:
                sub_str += ch
                visited.add(ch)
            # If the char is visited, update the sub_str_list and the max length
            else:
                if len(sub_str) > max_length:
                    if sub_str_list: sub_str_list.pop()
                    max_length = len(sub_str)
                    sub_str_list.append(sub_str)
                elif len(sub_str) >= max_length:
                    max_length = len(sub_str)
                    sub_str_list.append(sub_str)
                break
    return sub_str_list, len(sub_str_list[0])


def longest_unique_substr_linear(string):
    # last index of every character
    last_idx = {}
    max_len = 0

    # starting index of current window to calculate max_len
    start_idx = 0

    for i in range(0, len(string)):

        # Find the last index of str[i]
        # Update start_idx (starting index of current window)
        # as maximum of current value of start_idx and last index plus 1
        if string[i] in last_idx:
            start_idx = max(start_idx, last_idx[string[i]] + 1)

        # Update result if we get a larger window
        max_len = max(max_len, i - start_idx + 1)

        # Update last index of current char.
        last_idx[string[i]] = i

    return max_len


longest_unique_substr("GEEKSFORGEEKS")
longest_unique_substr_linear("GEEKSFORGEEKS")
