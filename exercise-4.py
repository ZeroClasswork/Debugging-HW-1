"""
Exercise 4
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search."""
    if high == None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == element: 
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid)

    else: 
        return binary_search(arr, element, mid+1, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)

# PART 1:
# Here is the stack trace we get from running the program:
#   File "/Users/meganobryan/Development/MakeSchool/Term3/SPD2-31/SPD-2.3-Debugging-Steps-Lab/exercise-4.py", line 22
#     if high == None:
#                    ^
# IndentationError: unindent does not match any outer indentation level
# 
# According to the stack trace, there is an IndentationError on line 22. This is 
# likely due to the extra indent on line 21.

# PART 2:
# "Based on the error we get, let's try changing the indent of the top comment."
# 
# "Ok, now we get a new error - RecursionError because we reached too high of a 
# recursion depth."
# 
# "My assumption is that this is due to a missing base case."
# 
# "After walking through the problem, I see that the statement on line 37 will
# never allow for a last index to be arr[mid]. This is because mid stays the same
# in this case."

# THE FIX:
# Change 
# return binary_search(arr, element, mid, high)
# to
# return binary_search(arr, element, mid+1, high)