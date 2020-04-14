'''
Question:
There are three type of edits that can be performed on strings. Insert a character, remove a character or replace a
character. Given two strings, write a code to check if they are one or zero edits away.

Solution:

We can have two pivots traversing each string, they must have at most one difference and once that difference is found,
we change the pivots position based on the lens of both strings (i.e. if lens are same or different).

Time complexity: O(N) where N is the number of elements in the smaller (or any word if lens are equal) word.
Space Complexity: O(1)



Written by:
Victor Arango-Quiroga (vdarango@hotmail.com)
'''

def solution1(w1, w2):

    # If lens differ by more than 1 char, then False
    if abs(len(w1) - len(w2)) > 1: return False

    # if lens differ, then make w1 to be the longest string
    if len(w1) < len(w2) : w1, w2 = (w2, w1)

    # Initialize pivots
    p1 = 0
    p2 = 0
    found_f = False

    while p1 < len(w1) and p2 < len(w2):

        if w1[p1] == w2[p2]:
            p1 += 1
            p2 += 1
        else:
            if found_f: return False

            if len(w1) != len(w2):
                p1 += 1
            else:
                p1 += 1
                p2 += 1
            found_f = True
    return True



if __name__ == '__main__':
    word1 = str(input())
    word2 = str(input())
    print(solution1(word1,word2))