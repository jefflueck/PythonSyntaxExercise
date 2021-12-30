def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # YOUR CODE HERE
    # get half of the expected output
    # My attempt want to talk through with mentor
    # for num in nums:
    #   if lowest == num or highest == num:
    #     print(highest and lowest)

    #   exists_highest = highest >= num
    #   exists_lowest = lowest <= num
    #   if exists_highest == True:
    #     print(int(highest))
    #   elif exists_lowest == True:
    #     print(int(lowest))

    # Solution
    # for num in nums:
    #       if num >= lowest and num <= highest:
    #           print(f"{num} fits")


in_range([10, 20, 30, 40, 50], 15, 30)
