'''
Question:
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the
to hold the additional characters, and that you are given the "true" length of the string.

Example:
    Input: 'Mr John Smith    ', 13
    Output: 'Mr%20John%20Smith


Written by:
Victor Arango-Quiroga (vdarango@hotmail.com)
'''

def solution1(string, last_idx):
    '''

    Time Complexity: O(N) where N is the real length e.g. last_idx
    Space complexity: O(1) since the only memory used is for the pivots and we are replacing inplace.
    :param string:  list of chars where " " needs to be replaced by "%20" (e.g. 'Mr John Smith    ')
    :param last_idx: Real length of string e.g. 13 for 'Mr John Smith    '
    :return: String with %20 on the spaces e.g. Mr%20John%20Smith
    '''
    write_pivot = len(string) -1
    read_pivot = last_idx - 1
    while write_pivot >= 0 and read_pivot >=0:

        if string[read_pivot] == " ":
            # append %20
            string[write_pivot] = '0'
            string[write_pivot - 1] = '2'
            string[write_pivot - 2 ] = '%'
            write_pivot -= 3
        else:
            string[write_pivot] = string[read_pivot]
            write_pivot -= 1

        read_pivot -= 1

    return "".join(string)

if __name__ == '__main__':
    '''
    Example Input: (note: there are 4 empty spaces after the 'h' character) 
    Mr John Smith    
    13
    Example Output:
    Mr%20John%20Smith
    '''
    arg1 = list(input())
    arg2 = int(input())

    print(solution1(arg1, arg2))