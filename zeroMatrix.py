from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = set()
    columns = set()

    # j = len(matrix) - 1
    row_length = len(matrix[0])

    for j in range(len(matrix)):
        # if j == -1:
            # break
        for i in range(row_length):
            if matrix[j][i] == 0:
                rows.add(j)
                columns.add(i)
        # j-=1

    # import pdb;
    # pdb.set_trace()

    for c in columns:
        for i in range(row_length):
            matrix[i][c] = 0

    for r in rows:
        matrix[r] = [0] * row_length

    print(matrix)

setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])


