'''
Question:
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data
structures?

    Assumptions: String will contain ASCII Characters

    ASCII Character -> That means that each character can have 128 (2^7) possible values. Thus, the sting length is
    maximum 128 characters long.
    
'''

def solution(text):
    '''
    Using a Dictionary (hash table) to store letters while traversing string
    Time complexity: O(N), however N is less or equal to 128. Then we could say O(1)
    Space complexity: We are using a dictionary to store characters so it increases with N (O(N)) but it will not have
    more than 128 elements.
    '''
    if len(text) > 128: return False
    checker = {}
    for char in text:
        if char in checker:
            return False
        checker[char] = 1
    return True

def solution2(text):
    '''
    Using a list to mark characters in the string
    time complexity is same as solution 1
    space complexity is contant.
    '''
    if len(text) > 128: return False

    checker = [None]*128 # Creating a list of 128 empty spaces. Constant space complexity
    for letter in text:
        if checker[ord(letter)] != None: return False
        checker[ord(letter)] = 1
    return True

def solution3(text):
    '''
    Binary vector solution. Similar to solution2, but instead of using a list of 128 elements, I use a binary number
    implementation which saves space.
    '''

    if len(text) > 128: return False

    binary_checker = 0
    for letter in text:
        if 1 << ord(letter) & binary_checker: return False
        binary_checker |= 1 << ord(letter)
    return True

def solution4_NoDataStructures(text):
    '''
    In this case, we can sort the string first (O(Nlog(N)) and then check if the next two consecutive chars are
    equal (O(N))
    Time Complexity: O(Nlog(N))
    Space Complexity: O(1)
    '''
    if len(text) > 128: return False
    text = sorted(text) # Sorting input O(Nlog(N))
    for index in range(len(text)-1): # Going up to the second to last one
        if text[index] == text[index+1]: return  False
    return True

if __name__ == '__main__':

    arg = str(input())
    print(solution(arg))
    print(solution2(arg))
    print(solution3(arg))
    print(solution4_NoDataStructures(arg))

