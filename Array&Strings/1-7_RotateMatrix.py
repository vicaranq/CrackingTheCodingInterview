'''
Question:
Given an image represented by a NxN matrix, where each pixel in the image is represented by an integer, write a method
to rotate the image by 90 degrees. Can you do this in place?

Solution 1:
We can rotate the matrix 90d egrees by first swaping all elements over the diagonal and then swap the outer columns
e.g.:
 [1, 2, 3]                          [1, 4, 7]                           [7, 4, 1]
 [4, 5, 6]   -- swap ver diag -->   [2, 5, 8]  -- swap columns -->      [8, 5, 2]
 [7, 8, 9]                          [3, 6, 9]                           [9, 6, 3]

time complexity: O(MxN)
space complexity: O(1) since all operations are performed inplace


Written by:
Victor Arango-Quiroga (vdarango@hotmail.com)
'''

def solution1(matrix):

    # check that it is a square Matrix
    if len(matrix) != len(matrix[0]): return False
    # swap over diagonal
    swapOverDiag(matrix)
    # swap columns
    swapColumns(matrix)
    return matrix

def swapOverDiag(matrix):
    ''' swap over diagonal in place'''
    n = len(matrix) # squared matrix nxn
    for i in range(n): # loop through columns
        for j in range(i+1,n): # loop through diagonal to end
            # swap over diagonal
            matrix[i][j], matrix[j][i] = (matrix[j][i], matrix[i][j])

def swapColumns(matrix):
    ''' swap columns from the outside to the inside e.g. 1st <-> end then 2nd <-> 2nd to last one, ....'''
    front_pivot = 0
    end_pivot = len(matrix[0]) -1
    while end_pivot>front_pivot:
        for i in range(len(matrix)):
            matrix[i][front_pivot], matrix[i][end_pivot] = ( matrix[i][end_pivot], matrix[i][front_pivot])
        front_pivot += 1
        end_pivot -= 1

if __name__ == "__main__":

    # 3x3 case
    matrix = [ [1, 2 ,3],
               [4, 5, 6],
               [7, 8, 9]]

    print('\n'.join(map(str,matrix)))
    print('\n'.join(map(str,solution1(matrix))))

    # 4x4 case
    matrix = [ [1, 2  , 3, 4 ],
               [5, 6  , 7, 8 ],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]

    print('\n'.join(map(str,matrix)))
    print('\n'.join(map(str,solution1(matrix))))
