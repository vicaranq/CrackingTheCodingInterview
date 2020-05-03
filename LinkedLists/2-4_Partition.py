'''
Question: Write code to partition a linked list around a value x, such that all nodes less than x come before all the
nodes greater than or equal to x. (IMPORTANT: The partition element x can appear anywhere in the "right partition";
it does not need to appear between the left and right partitions.

Example:
    Input 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
    3 5 8 5 10 2 1
    5

    Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
    1->2->3->5->8->5->10->
'''

def solution(head, partition):

    head2 = Node(head.data)

    LP = head2
    RP = head2

    node = head.next

    while node != None:
        next_node = node.next
        # check which partition the node correspond to
        if node.data < partition : # if true corresponds to left partition
            node.next = LP
            LP = node

        else:
            RP.next = node
            RP = RP.next

        node = next_node
    RP.next = None
    return LP

class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


if __name__ == '__main__':

    ll_elements = list(map(int,input().split()))
    partition_k = int(input())

    head = Node(ll_elements[0])
    node = head
    for element in ll_elements[1:]:
        node.next = Node(element)
        node = node.next

    n = head
    while n != None:
        print(n.data,end="->")
        n = n.next

    head2 = solution(head,partition_k)

    print()
    n = head2
    while n != None:
        print(n.data,end="->")
        n = n.next





