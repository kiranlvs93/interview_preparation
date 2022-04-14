# Given a list a1 and a2

import itertools


def get_pairs_using_for_loop(arr1: list, arr2: list, inp: int):
    """
    Using two for loops to get the pairs
    Time complexity - O(n^2)
    :param arr1:
    :param arr2:
    :param inp:
    :return:
    """
    # Maximum difference can be equal to input only even if the pair has 0,0
    diff = inp
    pairs = []
    # Use 2 for loops to get a pair
    for n1 in arr1:
        for n2 in arr2:
            sum_of_nos = n1 + n2
            # If the absolute diff b/w the sum of pair and inp is less than prev diff
            # Clean and update the new one
            if abs(sum_of_nos - inp) < diff:
                pairs.clear()
                pairs.append((n1, n2))
                diff = abs(sum_of_nos - inp)
            # If the absolute diff b/w the sum of pair and inp is equal to the prev diff
            # append the pair and dont pop the old one as the diff is same
            elif abs(sum_of_nos - inp) == diff:
                pairs.append((n1, n2))
                diff = abs(sum_of_nos - inp)
    # Final list will have only the pairs with min diff
    return pairs


def get_pairs_using_itertools(arr1: list, arr2: list, inp: int):
    """
    Use itertools to get all the combinations from two lists
    :param arr1:
    :param arr2:
    :param inp:
    :return:
    """
    diff = inp
    all_pairs = list(itertools.product(arr1, arr2))
    pair_diff = {}
    for pair in all_pairs:
        if abs(sum(pair) - inp) <= diff:
            diff = abs(sum(pair) - inp)
            pair_diff[pair] = diff

    # Sort the pair_diff dict in ascending order of the values (diff)
    pair_diff = dict(sorted(pair_diff.items(), key=lambda x: x[1]))
    # Get the value of the first item in dictionary which indicates the minimum difference
    # If the value is equal to above number, then add it to the list and return this list
    return [pair for pair, diff in pair_diff.items() if diff == pair_diff[list(pair_diff.keys())[0]]]


if __name__ == '__main__':
    a1 = [1, 10, 15, 25, 28, 40, 30, 0]
    a2 = [2, 9, 20, 35, 41, 1, 31]
    inp_number = 31
    print("Pairs that give the minimum difference with the input are ->", get_pairs_using_for_loop(a1, a2, inp_number))
    print("Pairs that give the minimum difference with the input are ->", get_pairs_using_itertools(a1, a2, inp_number))
