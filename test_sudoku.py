"""
    Unit Tests for Sudoku
"""
import sudoku


class TestSudoku:

    def test_solved(self):
        """
            Test that a solved puzzle will be marked solved
        """
        # solved sudoku puzzle
        grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [3, 1, 2, 8, 4, 5, 9, 6, 7],
                [6, 9, 7, 3, 1, 2, 8, 4, 5],
                [8, 4, 5, 6, 9, 7, 3, 1, 2],
                [2, 3, 1, 5, 7, 4, 6, 9, 8],
                [9, 6, 8, 2, 3, 1, 5, 7, 4],
                [5, 7, 4, 9, 6, 8, 2, 3, 1]]

        assert sudoku.is_solved(grid)

    def test_column_not_solved(self):
        """
            Test that columns with the same values will not be solved
        """
        grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9]]

        assert not sudoku.is_solved(grid)

    def test_row_not_solved(self):
        """
            Test that rows with the same values will not be solved
        """
        grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                [2, 2, 2, 2, 2, 2, 2, 2, 2],
                [3, 3, 3, 3, 3, 3, 3, 3, 3],
                [4, 4, 4, 4, 4, 4, 4, 4, 4],
                [5, 5, 5, 5, 5, 5, 5, 5, 5],
                [6, 6, 6, 6, 6, 6, 6, 6, 6],
                [7, 7, 7, 7, 7, 7, 7, 7, 7],
                [8, 8, 8, 8, 8, 8, 8, 8, 8],
                [9, 9, 9, 9, 9, 9, 9, 9, 9]]
        assert not sudoku.is_solved(grid)

    def test_incomplete_solution(self):
        """
            Test that an incomplete solution will be marked unsolved
        """
        grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [7, 8, 9, 1, 2, 3, 4, 5, None],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [3, 1, 2, 8, 4, 5, 9, 6, 7],
                [6, 9, 7, 3, 1, 2, 8, 4, 5],
                [8, 4, 5, 6, 9, 7, 3, 1, 2],
                [2, 3, 1, 5, 7, 4, 6, 9, 8],
                [9, 6, 8, 2, 3, 1, 5, 7, 4],
                [None, 7, 4, 9, 6, 8, 2, 3, 1]]

        assert not sudoku.is_solved(grid)
