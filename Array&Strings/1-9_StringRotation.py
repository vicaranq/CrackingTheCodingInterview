'''
Question:
String Rotation: Assume you have a method isSubstring() which checks if one word is a substring of the other. Given two
strings. s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g. waterbottle,
erbottlewat)

Solution:
s1 = waterbottle
s2 = erbottlewat

s1 = 'wat' + 'erbottle' = x + y = xy
s2 = 'erbottle + 'wat'  = y + x = yx

let's define s1' =s1+s1
s1' = s1s1 = xyxy which is equivalent to x + yx + y = x + s2 + y = xs2y
Thus, s2 is subString of s1s1.

'''


def isSubstring(s1, s2):
    ''' returns True if s1 is substring of s2'''
    return s1 in s2


def solution(s1,s2):

    if len(s1) != len(s2) or len(s1) == 0: return False

    s1 += s1

    return isSubstring(s2, s1)

if __name__ == '__main__':
    s1 = str(input())
    s2 = str(input())

    print(solution(s1,s2))