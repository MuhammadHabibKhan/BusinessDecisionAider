# Current Version: 2.0
# Dev: m.h.k

def input_matrix(nr, nc):
    """
        Purpose: To take input matrix to work function
        Input Parameters: number of rows and columns
        Pre-Condition: nr and nc must be non-zero
        In-case of Violation: See Line 8-11
    """
    if nc == 0 and nr == 0:
        return 'Please enter non-zero value for number of rows and columns'
    if nr == 0:
        return 'Please enter non-zero value for number of rows'
    elif nc == 0:
        return 'Please enter non-zero value for number of columns'
    else:
        matrix = []
        r = 0
        while r < nr:
            r_matrix = []
            c = 0
            while c < nc:
                a = float(input("Enter value for r" + str(r + 1) + "c" + str(c + 1) + ": "))
                r_matrix.append(a)
                c = c + 1
            matrix.append(r_matrix)
            r = r + 1
        return matrix


def print_matrix(mat):
    """
            Purpose: To print input matrix in matrix form
            Input Parameters: matrix (list of list)
    """
    n_rows = len(mat)
    n_col = len(mat[0])
    r = 0
    while r < n_rows:
        c = 0
        while c < n_col:
            print("%.3f" % mat[r][c], end="\t\t")
            c = c + 1
        print()
        r = r + 1


def reduce_to_one(mat, pr, pc):
    """
         Purpose: To make the pivot equal to 1 and carry out the function through the rest of the row
         Input Parameters: matrix (list of list), row of the element to be pivoted (pr)
         Pre-Condition: Pivot should not be zero already as division by zero would lead to undefined value
         In-case of Violation: See Line 54: if condition set to skip the value when element is zero
     """
    nr = len(mat)
    nc = len(mat[0])
    if mat[pr][pc] != 0:  # if pivot is zero, it should be skipped as dividing by zero would result in math error
        pivot = mat[pr][pc]  # storing original pivot value in variable to use it later
        mat[pr][pc] = mat[pr][pc] / mat[pr][pc]  # dividing by itself to make it 1
        # by pivot inverse
        for j in range(nc):  # iterating on number of columns to make each member of row divide by pivot inverse
            if pc != j:  # condition to skip j = 0 as it would mean the first pivot which is defined above
                mat[pr][j] = round(mat[pr][j] / pivot, 3)
                # division by original pivot of each member of row as done to the pivot
    return mat


def below_pivot_zero(mat, pr, pc, r):  # r is pivot element row, added for simplex to work
    """
          Purpose: To make the given element below pivot zero and carry the function through out the row
          Input Parameters: matrix (list of list), row of the element (pr), column of the element (pc)
          Pre-Condition: Element should not be zero and pr should not be equal to pc
          In-case of Violation: See Line 73: if condition set to skip those values
      """
    nr = len(mat)
    nc = len(mat[0])
    if mat[pr][pc] != 0:
        # if pr != pc or mat[pr][pc] != 0:  # condition that if k=i(diagonal) then it is already pivoted
        # M[k][i] = 0 means to skip if its already 0 given in question as division by zero is math error
        factor = mat[pr][pc]
        for j in range(0, nc):  # iterating on number of columns to advance in the same row
            t = mat[pr][j] - (factor * mat[r][j])  # multiplying by constant and subtract two rows rule
            mat[pr][j] = round(t, 3)
    return mat


def transpose(mat):
    """
              Purpose: To change the rows of a matrix into a column or vice versa
              Input Parameters: matrix (list of list)
              Pre-Condition: matrix should exist
              In-case of Violation: NameError Exception for non-existing matrix
    """
    n_rows = len(mat)
    n_col = len(mat[0])
    try:
        a = []
        t = []
        for i in range(n_rows):  # iterate on number of rows
            for j in range(n_col):  # iterate on number of columns
                a.append(mat[j][i])
        for g in range(0, len(a), n_rows):
            t.append(a[g:g + n_rows])
        return t
    except NameError:
        return "Invalid Matrix"


def mat_mul(mat1, mat2):
    """
              Purpose: To multiply two given matrices
              Input Parameters: matrix 1 & matrix 2 (list of list)
              Pre-Condition: number of columns of mat1 should equal to number of rows of mat2
              In-case of Violation: See Line: 114, 130, 131 ==> if else condition
    """
    nr1 = len(mat1)
    nc1 = len(mat1[0])
    nr2 = len(mat2)
    nc2 = len(mat2[0])
    if nc1 == nr2:
        result = []
        r = []
        for i in range(nr1):  # iterate on M rows
            for j in range(nc2):  # iterate on M1 columns
                for k in range(nr2):  # iterate on M1 rows
                    result.append(mat1[i][k] * mat2[k][j])  # appending the product of each multiplication, not adding
        q = 0
        re = []
        while q < nc2 * nr2 * nc2:
            ret = result[q:nc2+q]  # adding consecutive terms for the final multiplication result
            re.append(sum(ret))
            q = q + 3
        for g in range(0, len(re), nc2):
            r.append(re[g:g + nc1])
        return r
    else:
        return "Multiplication not possible"
