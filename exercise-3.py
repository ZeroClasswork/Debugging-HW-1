"""
Exercise 3
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

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
        while j >= 0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

# PART 1:
# Here is the stack trace we get from running the program:
# Traceback (most recent call last):
#   File "/Users/meganobryan/Development/MakeSchool/Term3/SPD2-31/SPD-2.3-Debugging-Steps-Lab/exercise-3.py", line 34, in <module>
#     answer = insertion_sort([5, 2, 3, 1, 6])
#   File "/Users/meganobryan/Development/MakeSchool/Term3/SPD2-31/SPD-2.3-Debugging-Steps-Lab/exercise-3.py", line 26, in insertion_sort
#     while key < arr[j] : 
# IndexError: list index out of range
# 
# According to the stack trace, there is an IndexError in line 26. This means that arr[j] is invalid because j is less than 0 or 
# greater than len(arr)-1. My guess is that j < 0 at the point of error and that key < arr[j] needs to be prevented from running in that case.

# PART 2:
# "To do insertion sort, we have to loop through the array and swap a given value 
# through the already sorted values prior to it until it gets to its right spot."
# 
# "We look at a key value, key, based on what index is next to be sorted, and the 
# value before it."
# 
# "Then we loop through any value before it that is greater than key, swaping the 
# values (or in this case, moving the prior values back and then inserting the key
# in its place) - this is where it goes wrong. The while loop can get an 
# IndexError in the while condition."

# THE FIX:
# Change
# while key < arr[j] : 
# to
# while j >= 0 and key < arr[j] : 