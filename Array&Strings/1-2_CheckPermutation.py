'''
Question:
Given two strings, write a method to decide if one is a permutation of the other.

Assumming ASCII, there are only 128 character choices, then we can have a vector counting frequency of a
character in one word and finally check its frequency in the other one

Possible Solution:
If one word is a permutation of the other, then they have the same character count. Meaning that 'god' and 'dog' have
both one 'g', one 'o', and one 'd'.


Written by:
Victor Arango-Quiroga (vdarango@hotmail.com)
'''



def solution1(word1, word2):
    '''
    Using list of 128 elements to count the frequency of each character in word 1, then the same list is check while
    iterating through word2 and we check if word2's char was counted previously, if true, then we decrease the count of
    that character, otherwise we return False because there is a mismatch of characters.

    We then check if the sum of checker is zero which means that all the characters in word1 where counter counted by
    word2. If there are still elements in the list, then there is a count mismatch and word1 is not a permutation of
    word2.

    Time complexity: O(N) where N is the size of word1 or word2 (both must be equal).
    Space Complexity: O(128) = O(1) because we are using a list of 128 elements.

    '''

    if len(word1) != len(word2): return False

    checker = [0]*128
    # First loop to create frequency of one word
    for char in word1:
        checker[ord(char)] += 1
    # second loop to check if char in word2 was counted in word1 and decrease its count
    for char in word2:
        if checker[ord(char)] != 0:
            checker[ord(char)] -= 1
        else:
            return False # Count in word1 is zero so they have different chars
    return True if sum(checker) == 0 else False

def solution2(word1, word2):
    '''
    Similar to solution 1, but here I use a number and use binary implementation to mimic previous approach with
    a list. Checks are easier to implement given the binary AND and OR operations. Time and space complexity are still
    the same, however this approach uses a lot less memory.
    '''
    if len(word1) != len(word2): return False

    binary_checker = 0

    for char in word1:
        binary_checker |= 1 << ord(char)
    for char2 in word2:
        binary_checker &= ~(1 << ord(char2)) # ones complement to create mask such as 111101111

    return False if binary_checker else True

if __name__ == '__main__':

    arg1 = str(input())
    arg2 = str(input())

    print(solution1(arg1,arg2))
    print(solution2(arg1,arg2))


