'''
Given a string, write a function to check if it is a permutation of a palindrome. You can ignore casing and non-letter
characters.

Example:
    Input: 'Tact Coa'
    Output: True  # because there is a permutation of the input that is a Palindrome (taco cat)

'''

def solution1(string):
    '''
    It will be a permutation of a palindrome if each character repeats an even number of times (even length) or only one
    element has not a corresponding pair (odd length). Thus we can count the frequency of a character and at the end we
    can check if all frequencies but at most one is an even number.

    This solution ignores casing, however, it counts all ASCII characters. Solution 2 only counts letters.

    Time complexity: O(N) where N is the length of the input string
    Space Complexity: O(1) because the freq_dict will have at most 128 key-value pairs assuming ASCII
    :param string: String to check
    :return: True, if it is a permutation of a Palindrome, otherwise False
    '''

    # Change to lower case and remove spaces
    string = string.lower().replace(' ','')
    print(string)
    num_odd_freq = 0
    freq_dict = {}

    for char in string:

        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1  # First time in dict

        if freq_dict[char] % 2 != 0:
            num_odd_freq += 1
        else:
            num_odd_freq -= 1
    print(num_odd_freq)
    return False if num_odd_freq > 1 else True

def charVal(char):
    val = ord(char)
    if val >= ord('a') and val <= ord('z'):
        return val - ord('a')
    return -1

def solution2(string):
    '''
    An extension of solution 1, but here we ignore non-letter characters. Additionally, I am using only an array of
    size 26.
    '''
    # Change to lowercase and replace spaces with empty space
    string = string.lower().replace(' ', '')
    english_alphabet = [0]*26
    odd_count = 0
    for char in string:
        val = charVal(char)
        if val != -1:
            # print(f'char is {char} and val is {val}')
            english_alphabet[val] += 1
            if english_alphabet[val] % 2 != 0:
                odd_count += 1
            else:
                odd_count -= 1

    return False if odd_count > 1 else True



if __name__ == '__main__':

    arg1 = str(input())
    print(solution1(arg1))
    print(solution2(arg1))