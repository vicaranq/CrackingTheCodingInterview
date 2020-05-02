'''
Question:  Implement an algorithm to delete a noded in the midle(i.e. any node but the first and last node, not necessarily
the exact middle) of a singly linked list, given only access to that node.
Example:
    Input: the node c from LL a ->  b -> c -> d -> e -> f
    Output: None but new LL must be  a ->  b -> d -> e -> f
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def solution(node):

    if node == None or node.next == None:
        return False

    # delete current node
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next

if __name__ == '__main__':

    input_ll = list(map(int,input().split()))
    head = Node(input_ll[0])
    node = head
    for data in input_ll[1:]:
        new_node = Node(data)
        node.next = new_node
        node = node.next # update node

    n = head
    while n != None:
        print(n.data,end="->")
        n = n.next

    solution(head.next)

    print()
    n = head
    while n != None:
        print(n.data,end="->")
        n = n.next