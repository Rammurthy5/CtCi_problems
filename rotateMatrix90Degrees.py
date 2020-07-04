"""
Rotate any NxN matrix to clockwise or anti-clockwise direction.

note: the following approach can be done only for NxN matrix ie. same no. of rows and cols.
Not for NxM matrix.


"""

# 1 2 3 4     3 9 5 1           3 4 5 6     3 9 5 1
# 5 6 7 8     4 0 6 2           9 0 6 2     4 0 1 2
# 9 0 1 2     5 1 7 3           5 1 7 8     5 6 7 3
# 3 4 5 6     6 2 8 4           1 2 3 4     6 2 8 4

# 1 2 3       7 2 1       7 4 1
# 4 5 6       4 5 6       8 5 2
# 7 8 9       9 8 3       9 6 3


def rotate_clockwise(matrix):

    # for layer in range(len(matrix) // 2):
    #     for ele in range(layer, len(matrix[layer])-1-layer):
    #         i, j = layer, ele
    #
    #         temp = matrix[i][j]
    #
    #         matrix[i][j] = matrix[~j][i]
    #         matrix[~j][i] = matrix[~i][~j]
    #         matrix[~i][~j] = matrix[j][~i]
    #         matrix[j][~i] = temp

    # 20 ms
    top, bottom = 0, len(matrix) - 1
    while top < bottom:
        tmp = matrix[top]
        matrix[top] = matrix[bottom]
        matrix[bottom] = tmp
        top += 1
        bottom -= 1

    for i in range(1, len(matrix)):
        for j in range(i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    import pdb; pdb.set_trace()
# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 10, 11], [12, 13, 14, 15]]


#
# 1 2 3 4         12 2 3 1        12 9 3 1        12 9 5 1            12 9 5 1
# 5 6 7 8         5 6 7 8         5 6 7 2         13 6 7 2            13 0 6 2
# 9 0 10 11       9 0 10 11       14 0 10 11      14 0 10 3           14 10 7 3
# 12 13 14 15     15 13 14 4      15 13 8 4       15 11 8 4           15 11 8 4

rotate_clockwise(mat)

# 1 2 3 4     3 9 5 1
# 5 6 7 8     4 0 6 2
# 9 0 1 2     5 1 7 3
# 3 4 5 6     6 2 8 4

# 1 2 3       7 4 1
# 4 5 6       8 5 2
# 7 8 9       9 6 3
