
'''
Question:
Implement a method to perform basic string compression using counts of repeated cheracters. For example, the string
aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your
method should return the original string. You can assume the string has only uppercase and lowecase letters.

Example1 :
    Input : aabcccccaaa
    Output  a2b1c5a3

Example2 :
    Input : aaaaaaaaaabbccd
    Output  a10b2c2d1
'''
import timeit


def solution1(string):

    temp_letter = string[0] # init to first letter
    count = 0
    string_compressed = ''

    for lett in string:

        if lett == temp_letter:
            count += 1
        else:
            # append to compressed string
            string_compressed += temp_letter + str(count)
            # update the variables
            temp_letter = lett
            count = 1

    string_compressed += temp_letter + str(count) # appending last letter and count

    return string_compressed if len(string_compressed) < len(string) else string


def solution2(string):
    '''
    more efficient concatenation
    :param string:
    :return:
    '''

    temp_letter = string[0] # init to first letter
    count = 0
    string_compressed = []

    for lett in string:

        if lett == temp_letter:
            count += 1
        else:
            # append to compressed string
            string_compressed.append(temp_letter)
            string_compressed.append(str(count))
            # update the variables
            temp_letter = lett
            count = 1

    string_compressed.append(temp_letter)
    string_compressed.append(str(count))

    return ''.join(string_compressed) if len(string_compressed) < len(string) else string

def solution3(string):
    ''' Check if compressed string is going to be smaller before creating the compresses string. Also, use the size info
    to create an empty array with proper size'''

    compressed_string_len = getCompressedLen(string)

    if compressed_string_len >= len(string): return string

    # Create list with proper space allocation
    string_compressed = [None]*compressed_string_len
    temp_letter = string[0]
    count = 0
    idx = 0
    for lett in string:

        if lett == temp_letter:
            count += 1
        else:
            # append to compressed string
            string_compressed[idx] = temp_letter
            for number in str(count):
                idx += 1
                string_compressed[idx] = number
            # update the variables
            temp_letter = lett
            count = 1
            idx += 1

    string_compressed[idx] = temp_letter
    for number in str(count):
        idx += 1
        string_compressed[idx] = number

    return ''.join(string_compressed)


def getCompressedLen(string):

    temp_letter = string[0]
    count = 0
    compressed_str_len = 0
    for char in string:
        if char == temp_letter:
            count +=1
        else:
            # increase by 1 char
            compressed_str_len += 1
            # increase by number of digits in count
            compressed_str_len += len(str(count))

            temp_letter = char
            count = 1
    # increase by 1 char
    compressed_str_len += 1
    # increase by number of digits in count
    compressed_str_len += len(str(count))

    return compressed_str_len

def timefunct(name):
    SETUP_CODE = f'''from __main__ import {name}'''

    TEST_CODE = \
        f'''
arg1 = ''.join(map(str, [ x for x in range(1000)]))
{name}(arg1)
        '''

    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 10000)
    return times

if __name__ =='__main__':
    print("Type input string:")
    arg1 = str(input())
    print(solution1(arg1))
    print(solution2(arg1))
    print(solution3(arg1))


    # test - worst case with 1k chars
    # times = timefunct('solution1')
    # print(f'solution1 time:  {min(times)}')
    #
    # times = timefunct('solution2')
    # print(f'solution2 time:  {min(times)}')

    # times = timefunct('solution3')
    # print(f'solution3 time:  {min(times)}')

    '''
    solution1 time:  14.6234589
    solution2 time:  12.434463800000003
    solution3 time:  11.5387766
    '''