'''
2.8 Loop Detection: Given a linked list which might contain a loop, implement an algorithm that returns the node at the
beginning of the loop (if one exists).

'''

from utils.classes import Node
# from utils.functions import createLL



def createLoop():

    h = Node("A")
    node = h
    start_node = None
    for letter in ["B", "C", "D", "E"]:
        node.next = Node(letter)
        if letter =="C": start_node = node.next
        node = node.next

    # generate loop
    node.next = start_node

    return h
def createLL(ll):

    head = Node(ll[0])
    node = head
    for n in ll[1:]:
        node.next = Node(n)
        node = node.next
    return head

def solution1(h):
    ''' time: O(N) where N is the number of non-repeated nodes
        space O(N)
    '''
    nodes = set()
    while h:
        if h in nodes:
            return h
        nodes.add(h)
        h = h.next
    return None

def solution2(h):

    s, f = (h, h)
    # find collision if f pointer goes 1 step faster than s pointer, they'll collide at LEN(LOOP) - k where k is
    # distance from head to start of the loop mod LEN(LOOP). Inside loop, f will get closet to s at a rate of 1 node/time

    while f.next and f.next.next:
        s, f = (s.next, f.next.next)
        if f == s: break


    # check if there is not a cycle
    if not f.next or not f.next.next:
        return None

    # collision is at s or f. Head and collision node are at the same distance from the start of the loop
    s = head
    while s and f:
        if s == f:
            return s
        s, f = (s.next, f.next)
    return False





if __name__ == '__main__':

    print( "Solution 1")
    ''' Loop Test A -> B -> C -> D -> E -> C (same object as previous C)'''
    head = createLoop()
    loop_head = solution1(head)
    print("Head of loop (if any): {}".format(loop_head.data))

    ''' Non-Loop Test   A -> B -> C -> D -> E'''

    head_non_cycle = createLL(['A','B','C','D','E'])
    loop_head = solution1(head_non_cycle)
    print("Head of loop (if any): {}".format(loop_head))

    ''' solution 2 '''
    print( "Solution 2")
    ''' Loop Test A -> B -> C -> D -> E -> C (same object as previous C)'''
    head = createLoop()
    loop_head = solution2(head)
    print("Head of loop (if any): {}".format(loop_head.data))

    ''' Non-Loop Test   A -> B -> C -> D -> E'''

    head_non_cycle = createLL(['A','B','C','D','E'])
    loop_head = solution2(head_non_cycle)
    print("Head of loop (if any): {}".format(loop_head))
