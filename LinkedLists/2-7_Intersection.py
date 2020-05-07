'''
Question: Given two singly linked list determine if the two lists intersect. Return the intersecting node. NOte that the
 intersection is defined based on reference and not the value. That is, if the kth node of the first linked list  is the
  same node by reference as the jth node of the second linked list, then they are intersecting.

'''
from utils.classes import Node
from utils.functions import printLL

# class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None
# def printLL(head):
#     node = head
#     while node != None:
#         print(node,end='->')
#         node = node.next
#     print()



def test1():
    ''' returns two intersected linked lists'''
    h1 = Node(3)
    h2 = Node(4)

    node = h1
    for i in [1, 5, 9]:
        node.next = Node(i)
        node = node.next
    last_h1 = node
    node = h2
    for i in [6]:
        node.next = Node(i)
        node = node.next
    last_h2 = node

    for i in [7, 2, 1]:
        n = Node(i)
        last_h1.next = n
        last_h2.next = n
        last_h2, last_h1 = (last_h2.next, last_h1.next)

    return (h1, h2)

def test2():

    h1 = Node(3)
    h2 = Node(4)

    node = h1
    for i in [1, 5, 9, 7, 2, 1]:
        node.next = Node(i)
        node = node.next

    node = h2
    for i in [6, 7, 2, 1]:
        node.next = Node(i)
        node = node.next

    return (h1, h2)

def solution1(h1, h2):
    ''' check if node is repeated: time complex O(N) space complex O(N)'''

    nodes = set()

    while h1 and h2:

        if h1 in nodes or h2 in nodes:
            return h1 if h1 in nodes else h2

        nodes.add(h1)
        nodes.add(h2)

        h1, h2 = (h1.next, h2.next)

    return None

def getLenAndLastNode(h):
    counter = 1
    while h.next:
        counter += 1
        h = h.next
    return (h, counter)

def solution2(h1, h2):
    ''' check if node is repeated: time complex O(N) space complex O(1)'''

    # check len of LLs and check if last node is the same, otherwise they are not intersected
    (lastNode1, len1) = getLenAndLastNode(h1)
    (lastNode2, len2) = getLenAndLastNode(h2)

    # if not intersection, then return None
    if lastNode1 != lastNode2: return None

    if len1 > len2:
        diff = len1 - len2
        while diff >0:
            h1 = h1.next
            diff -= 1
        print(" New h1 {}".format(h1.data))
    else:
        diff = len2 - len1
        while diff > 0:
            h2 = h2.next
            diff -= 1
        print(" New h2 {}".format(h2.data))

    # now they are same length from h1 and h2, we can compare node to node until intersection is found
    while h1 or h2:

        if h1 == h2:
            return h1

        h1 = h1.next
        h2 = h2.next

    return False





if __name__ == '__main__':

    print('----solution2 time: O(N) | space: O(N)-----')
    h1, h2 = test1()
    printLL(h1)
    printLL(h2)

    repeated = solution1(h1, h2)

    print("Repeated is: {}".format(repeated.data if repeated else None))


    h1, h2 = test2()
    printLL(h1)
    printLL(h2)
    repeated = solution1(h1, h2)

    print("Repeated is: {}".format(repeated.data if repeated else None))

    print('----solution2 time: O(N) | space: O(1)-----')

    h1, h2 = test1()
    printLL(h1)
    printLL(h2)

    repeated = solution2(h1, h2)

    print("Repeated is: {}".format(repeated.data if repeated else None))


    h1, h2 = test2()
    printLL(h1)
    printLL(h2)
    repeated = solution2(h1, h2)

    print("Repeated is: {}".format(repeated.data if repeated else None))






