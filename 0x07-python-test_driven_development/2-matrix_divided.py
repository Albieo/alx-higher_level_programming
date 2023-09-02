#!/usr/bin/python3
""" Divide a matrix """


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a specified divisor.

    This function takes a matrix (list of lists) and a divisor (number), and
    returns a new matrix where each element of the input matrix is divided
    by the divisor.

    Args:
    matrix (list of lists): The input matrix to be divided.
                            Each inner list represents a row, and
                            all rows must have the same number of elements.
    div (int or float): The divisor by which each element in the matrix will
                        be divided. It mustbe a non-zero number.

    Returns:
    list of lists: A new matrix where each element is the result of dividing
                   the corresponding element from the input matrix by the
                   divisor. The resulting elements are rounded to
                   2 decimal places.

    Raises:
    TypeError: If the input matrix is not a valid matrix (list of lists) of
               integers/floats, if the divisor is not a number, or if the rows
               of the matrix have different sizes.
    ZeroDivisionError: If the divisor is zero.

    """
    new_matrix = []
    first_row_length = len(matrix[0])
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) == list:
        for i in range(len(matrix)):
            if type(matrix[i]) == list:
                for j in range(len(matrix[i])):
                    if not isinstance(matrix[i][j], (int, float)):
                        raise TypeError(matrix_error)
            else:
                raise TypeError(matrix_error)

    for row in matrix:
        if len(row) != first_row_length:
            raise TypeError("Each row of the matrix must have the same size")
    else:
        for i in range(len(matrix)):
            new_row = []
            for j in range(len(matrix[i])):
                new_row.append(round(matrix[i][j] / div, 2))
            new_matrix.append(new_row)
        return new_matrix
