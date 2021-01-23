"""
Exercise 1
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

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums)-1):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)


# PART 1:
# Here is the stack trace we get from running the program:
# Traceback (most recent call last):
#   File "/Users/meganobryan/Development/MakeSchool/Term3/SPD2-31/SPD-2.3-Debugging-Steps-Lab/exercise-1.py", line 31, in <module>
#     answer = find_largest_diff([5, 3, 1, 2, 6, 4])
#   File "/Users/meganobryan/Development/MakeSchool/Term3/SPD2-31/SPD-2.3-Debugging-Steps-Lab/exercise-1.py", line 23, in find_largest_diff
#     diff = abs(list_of_nums[i] - list_of_nums[i+1])
# IndexError: list index out of range
# 
# According to the stack trace, there is an IndexError on line 23. This means that list_of_nums[i] or list_of_nums[i+1] is invalid 
# because i or i+1 is greater than len(list_of_nums)-1 or less than 0. My guess is that i+1 is going up to len(list_of_nums) which makes
# list_of_nums[i+1] out of range. 

# PART 2:
# "The function attempts to find the largest difference between consecutive numbers"
# 
# "The smallest difference possible between 2 numbers is zero so setting largest_diff to 0 makes sense"
# 
# "We have to loop through the entire list so going through the range of 0 to len(list_of_nums)-1 makes sense
# EXCEPT that we're comparing two numbers so we need to go through one less number since we compare to i+1 in 
# the next line."

# THE FIX:
# I changed line 22 from
# for i in range(len(list_of_nums)):
# to
# for i in range(len(list_of_nums)-1):
