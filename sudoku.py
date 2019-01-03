
def grid_str(grid):
    square_len = int(pow(len(grid), 0.5))
    row_strings = []
    for row in grid:
        tmp_strings = []
        for i in range(0, len(row), square_len):
            tmp_strings.append(" | ".join([str(c) if c is
                               not None else ' ' for c in
                               row[i:i+square_len]]))
        row_strings.append(" || ".join(tmp_strings))
    sep = "\n" + ("-" * len(row_strings[0])) + "\n"
    third_sep = "\n" + ("=" * len(row_strings[0])) + "\n"
    tmp_rows = []
    for i in range(0, len(row_strings), square_len):
        tmp_rows.append(sep.join(row_strings[i:i+square_len]))
    return third_sep.join(tmp_rows)


def is_solved(grid):
    """
    This functions works by making all rows and columns into sets and then
    validating that they contain the complete ranage of values

    Individual squares do not have to be validated because if columns and rows
    are all unique, then squares will be unique as well.

    Parameters:
        grid : NxN list of lists that contains int and None values

    Returns True if the grid is solved, False otherwise
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


def csp_search(grid):
    """
    This function will solve the puzzle using the func parameter to create
    values.

    Parameters:
        grid : NxN list of lists that contains int and None values

    Yields an assignment tuple of the form (row, column, assignment)

    Note: Constraint Satisfaction problems can be solved by eliminating the
    domains of values based on the constraints of the problem. Sudoku's
    constraints are that each value assignment must be unique to its row,
    column, and square. Many of these problems can be solved by simple domain
    reduction, but some values must be deduced by inference of the constraints
    of its neighbors.
    For example: The left-most square is missing {2, 4, 8}. By reducing each of
    their domains, we get their domains as {2, 4}, {2, 4, 8}, and {2, 4}, from
    top to bottom. We know that the square is missing an 8 and the only
    position that can still take that value is the middle one of the left
    square.
        _______________________________________
        | 1 |   | 3 ||   | 5 | 6 || 7 | 8 | 9 |
        | 7 |   | 9 || 1 |   | 3 ||   | 5 | 6 |
        |   | 5 | 6 || 7 | 8 | 9 || 1 |   | 3 |
        _______________________________________
    """
    def square_index(row, col):
        return ((row // square_len) * square_len) + col // square_len

    def gen_row_col_in_square(index):
        row_range = (index // square_len) * square_len
        col_range = (index % square_len) * square_len
        for r in range(row_range, row_range + square_len):
            for c in range(col_range, col_range + square_len):
                yield r, c

    def gen_row_col_in_row(row):
        for col in range(0, len(grid)):
            yield row, col

    def gen_row_col_in_col(col):
        for row in range(0, len(grid)):
            yield row, col

    def get_possibilities(row, col):
        sq_index = square_index(row, col)
        return row_sets[row] & col_sets[col] & square_sets[sq_index]

    def remove_value_from_sets(row, col, assignment):
        # Update our missing sets after an assignment
        row_sets[row].remove(assignment)
        col_sets[col].remove(assignment)
        square_sets[sq_index].remove(assignment)

    square_len = int(pow(len(grid), 0.5))
    complete_set = set(range(1, len(grid) + 1))
    unassigned_locs = set()
    # Generate requirements sets for all rows
    row_sets = tuple([complete_set.difference(set(row),
                     {None}) for row in grid])

    # Generate requirements sets for all columns
    col_sets = []
    for i in range(len(grid)):  # col iterator
        col_set = set()
        for j in range(len(grid)):  # row iterator
            if grid[j][i] is None:
                unassigned_locs.add((j, i))
            else:
                col_set.add(grid[j][i])
        col_sets.append(complete_set.difference(col_set, {None}))
    col_sets = tuple(col_sets)

    square_sets = []
    for r in range(0, len(grid), square_len):
        for c in range(0, len(grid), square_len):
            square_set = set()
            for sub_row in range(square_len):
                square_set.update(grid[r + sub_row][c:c + square_len])
            square_sets.append(complete_set.difference(square_set, {None}))
    square_sets = tuple(square_sets)

    assigning_values = True
    while assigning_values:
        assigning_values = False
        for row, col in unassigned_locs:
            sq_index = square_index(row, col)
            loc_set = get_possibilities(row, col)
            if len(loc_set) == 1:
                assigning_values = True
                assignment = loc_set.pop()
                remove_value_from_sets(row, col, assignment)
                yield row, col, assignment
                unassigned_locs.remove((row, col))
                # break to avoid error from changing the set during iteration
                break
        if not assigning_values:
            for row, col in unassigned_locs:
                sq_index = square_index(row, col)
                generators = [gen_row_col_in_square(sq_index),
                              gen_row_col_in_row(row),
                              gen_row_col_in_col(col)]
                for generator in generators:
                    other_union = set()
                    assigned_set = set()
                    for other_row, other_col in generator:
                        if other_row != row or other_col != col:
                            if grid[other_row][other_col] is None:
                                other_union |= get_possibilities(other_row,
                                                                 other_col)
                            else:
                                assigned_set.add(grid[other_row][other_col])
                    possibilities = complete_set - assigned_set - other_union
                    if len(possibilities) == 1:
                        assigning_values = True
                        assignment = possibilities.pop()
                        remove_value_from_sets(row, col, assignment)
                        yield row, col, assignment
                        unassigned_locs.remove((row, col))
                        break
                if assigning_values:
                    break


def solve(grid, func=csp_search):
    """
    This function will solve the puzzle using the func parameter to create
    values.

    Parameters:
        grid : NxN list of lists that contains int and None values
        func : generator that takes a grid and returns a tuple,
            (row, col, assigment)

    Returns the solved grid
    """
    for row, col, assignment in func(grid):
        # print (row, col, assignment)
        grid[row][col] = assignment
        # print(grid_str(grid))
        # print()

    return grid
