"""
Created on 03/26/2017
@author: Simon
"""

def get_all_subsets(some_list):
    """
    return all subsets of size 0 -len(some_list) for some_list
    """
    if len(some_list) == 0:
        # If the list is empty, return the empty list.
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        subsets.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset)
    return subsets


NUMBER = 3
def look_for_all_the_things(my_list):
    """Looks at all subsets of this list"""
    # Make subsets
    all_subsets = get_all_subsets(my_list)
    print all_subsets
    for subset in all_subsets:
        if sum(subset) == NUMBER:
            # print subset
            return True
    return False

# myList = [1,2,3,4,5,6,7,8,9,10]
# print look_for_all_the_things(myList)
