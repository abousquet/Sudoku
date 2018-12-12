
def is_solved(grid):
    """
    This functions works by making all rows and columns into sets and then
    validating that they contain the complete ranage of values

    Individual squares do not have to be validated because if columns and rows
    are all unique, then squares will be unique as well.

    Parameters:
        grid : NxN list of lists that contains numerical values and None
    """
    # Create a complete set of all values that should be in each row, col, or s
    # square
    complete_set = set(range(1, len(grid) + 1))

    # Check rows
    for row in grid:
        if set(row) != complete_set:
            return False

    # Check columns
    for column in range(len(grid)):
        if set([row[column] for row in grid]) != complete_set:
            return False

    return True
