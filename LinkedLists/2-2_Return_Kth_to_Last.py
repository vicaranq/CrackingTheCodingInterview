'''
Question: Implement an algorithm to find the kth to last element of a singly linked list.
k = 1 returns last element
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def solution1( head, k):
    result = []
    sol_recursive(head, k, result)

    return result[0] if result else None

def sol_recursive(node, k , result):

    if node == None:
        return 0

    temp = sol_recursive(node.next, k, result) + 1

    if temp == k:
        result.append(node.data)

    return temp

if __name__ == '__main__':

    temp_list = list(map(int,input().split()))
    k = int(input())

    head = Node(temp_list[0])
    node = head
    for element in temp_list[1:]:
        n = Node(element)
        node.next = n
        node = n

    node = head
    while node != None:
        print(node.data, end="->")
        node = node.next

    print( "The Kth to the last element is: {} ".format(solution1(head,k)))
