"""
Exercise 2
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

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True

# PART 1:
# The expected output for this problem is False; True but it outputs False; False.
# The problem is at line 25, the first else statement, because it causes the output 
# to be False if the first three aren't consecutive instead of checking each set of 
# 3 numbers.

# PART 2:
# "The function should return two if the list contains 3 consecutive numbers next 
# to each other."
# 
# "We have to loop through, using indeces and only to the third to last value, so 
# the for loop is setup correctly."
# 
# "The if statement compares the number at the index to the next two numbers and 
# returns True if they form the consecutive chain we're looking for - so that 
# checks out."
# 
# "Ah, but this 'else' shouldn't be here. False is only confirmed once the True 
# is ruled out for *each* triad."

# THE FIX:
# Got rid of the first else statement.