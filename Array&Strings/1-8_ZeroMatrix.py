'''
Question:
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

Solution:
We can iterate through the matrix and record in two lists what cols/rows need to be zero. Then we can iterate again
and zero the cols and rows as needed

Time complexity: O(M * N) which is the minimum we can do since we have to visit all elements in the matrix.
Space complexity: O(max(M,N)) since we are using lists to store rows and cols that need to be zero. In the worst case
                  the vectors will have a max len of the longest dimension.
'''


def solution1(matrix):

    cols =[]
    rows = []

    m = len(matrix)
    n = len(matrix[0])

    # Find rows and cols that need to be zero
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                cols.append(j)
                rows.append(i)

    # zero rows
    for row in rows:
        zero_row(matrix,row,n)

    # zero cols
    for col in cols:
        zero_col(matrix,col, m)

    return matrix

def zero_row(matrix, row, n):
    matrix[row] = [0]*n

def zero_col(matrix, col, m):
    for i in range(m):
        matrix[i][col] = 0



if __name__ == '__main__':

    matrix = [[1,1,0],
              [1,1,1],
              [1,0,1]]
    print('\n'.join(map(str,solution1(matrix))))

    matrix = [[1,1,1,1,1,1],
              [1,1,1,1,1,1],
              [1,1,1,0,1,1]]

    print('\n'.join(map(str,solution1(matrix))))