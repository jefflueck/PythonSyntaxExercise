def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    # My original code verses this solution code had the while loop incorrectly set by syntax. Understand my error.
    # This works as expected.
    while start <= stop:
        print(start)
        start = start + 1




count_up(5, 7)
