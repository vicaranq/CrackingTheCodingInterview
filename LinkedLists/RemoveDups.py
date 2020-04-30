'''

Question: Write code to remove duplicates from an unsorted linked list.
Follow Up: How would you solve this problem if a temporary buffer is not allowed? -> N^2 solution to find repeated for each element.

Answer:
Keep a dictionary having data that has been visited, if found again, then remove.
'''
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:

    def __init__(self, node):
        self.head = node


def solution1(ll):
    ''' Get rid of duplicates'''
    node = ll.head
    data_dict = {}
    prev_node = None
    while node != None:
        if node.data not in data_dict:
            data_dict[node.data] = 1
            prev_node = node # only update prev_node if we are not removing
        else:
            prev_node.next = node.next

        node = node.next


if __name__ == '__main__':

    # generate linked list
    in_list = list(map(int, input().split()))
    head = Node(in_list[0])
    ll = linkedList(head)
    node = head
    for number in in_list[1:]:

        node.next = Node(number)
        node = node.next

    node = ll.head
    while node != None:
        print(node.data, end="->")
        node = node.next

    solution1(ll)
    print()

    node = ll.head
    while node != None:
        print(node.data, end="->")
        node = node.next
