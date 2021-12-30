def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE
    # Solution code, mine was very close but did not have the extra return or the False outdented.
    for num in nums:
        if num == 7:
            return True
    # Why do we need this return and outdenting
    return False
print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

