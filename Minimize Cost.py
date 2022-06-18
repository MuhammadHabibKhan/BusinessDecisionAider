# Program for finding the optimal solution of a given Linear Programming Problem using Simplex Method:
# Dev: mhk
# for maximize

from ElementaryRowOperations import *


def pivot_column(mat):
    nc = len(mat[0])
    maximum = mat[0][0]
    m_index = 0
    for i in range(nc):
        if mat[0][i] > maximum:
            maximum = mat[0][i]
            m_index = i
    if maximum > 0:
        return m_index + 1


def pivot_row(mat, m_index):
    nc = len(mat[0])
    nr = len(mat)
    lowest_ratio = mat[1][nc - 1] / mat[1][m_index - 1]
    row_index = 0
    for i in range(1, nr):
        if mat[i][nc - 1] / mat[i][m_index - 1] < lowest_ratio:
            lowest_ratio = mat[i][nc - 1] / mat[i][m_index - 1]
            row_index = i
    if lowest_ratio > 0:
        return row_index + 1


mat = [[4, 3, 0, 0, 0],
       [2, 1, -1, 0, 8], [2, 2, 0, -1, 10]]

nc = len(mat[0])
nr = len(mat)

while True:
    a = pivot_column(mat)
    b = pivot_row(mat, a)
    print("Pivot Element's Coordinates are: ")
    print(b)
    print(a)
    print()
    c = reduce_to_one(mat, b - 1, a - 1)
    # for h in range(nr):
    # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    # print_matrix(c)
    # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    # print()
    for h in range(nr - 1):  # -2 instead of -1 as we have labels now too
        # pr = int(input('Enter pr: '))
        # pc = int(input('Enter pc: '))
        d = below_pivot_zero(c, b - 1 - h - 1, a - 1, b - 1)
        # print()
        # print("```````````````````````````````````````````````````````````````````````")
        # print_matrix(d)
        # print("```````````````````````````````````````````````````````````````````````")
        # print()
    if d[0][0] <= 0 and d[0][1] <= 0:
        break

print_matrix(d)
