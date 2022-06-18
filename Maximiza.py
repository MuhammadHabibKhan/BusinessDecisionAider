# Program for finding the optimal solution of a given Linear Programming Problem using Simplex Method:
# Dev: mhk
# for maximize

from ElementaryRowOperations import *


def pivot_column(mat):
    nc = len(mat[0])
    minimum = mat[nr-1][0]
    m_index = 0
    for i in range(1, nc):
        if mat[nr-1][i] < minimum:
            minimum = mat[nr-1][i]
            m_index = i
    if minimum < 0:
        return m_index+1


def pivot_row(mat, m_index):
    nc = len(mat[0])
    nr = len(mat)
    lowest_ratio = mat[0][nc-1]/mat[0][m_index-1]
    row_index = 0
    for i in range(1, nr-1):
        if mat[i][nc-1]/mat[i][m_index-1] < lowest_ratio:
            lowest_ratio = mat[i][nc-1]/mat[i][m_index-1]
            row_index = i
    if lowest_ratio > 0:
        return row_index+1


# mat = [[-5, -10, 0, 0, 0, 0], [20, 10, 1, 0, 0, 200], [10, 20, 0, 1, 0, 120], [10, 30, 0, 0, 1, 150]]
mat = [[2, 3, 2, 1, 0, 0, 1000], [1, 1, 2, 0, 1, 0, 800], [-7, -8, -10, 0, 0, 1, 0]]

nc = len(mat[0])
nr = len(mat)

while True:
    a = pivot_column(mat)
    if a is None:
        break
    b = pivot_row(mat, a)
    print("Pivot Element's Coordinates are: ")
    print(b)
    print(a)
    print()
    c = reduce_to_one(mat, b-1, a-1)
    for h in range(nr-1):  # -2 instead of -1 as we have labels now too
        d = below_pivot_zero(c, b-1-h-1, a-1, b-1)
        print_matrix(d)
        print()
    for k in range(nc-1):
        if d[nr-1][k] >= 0:
            break

# print_matrix(d)
