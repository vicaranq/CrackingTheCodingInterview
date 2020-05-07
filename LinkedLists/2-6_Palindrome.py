'''
    2.6 Implement a function to check if a linked list is a palindrome
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def solution1(head):
    ''' Implementing an iterative approach to find where the middle is using a slow and fast pivots. I create a stack
    and append values while iterating to half of the list. Then, I start checking top of the stack with next elements of
     slow pivot. Check is done for the ODD case. '''
    s, f = (head, head)
    stack = []

    while s:
        stack.append(s.data)

        if f.next and f.next.next:
            f = f.next.next
        else:
            break
        s = s.next

    if not f.next: # odd length
        stack.pop()

    s = s.next

    while s:
        if s.data != stack.pop():
            return False
        s = s.next
    return True


class LL:
    def __init__(self, node):
        self.head = node
        self.tail = node

def rec_reverse(n):

    if not n.next:
        ll = LL(Node(n.data))
        return ll

    ll = rec_reverse(n.next)
    nn = Node(n.data)
    ll.tail.next = nn
    ll.tail = nn
    return ll

def iter_reverse(n):
    head = None
    while n != None:
        nn = Node(n.data)
        nn.next = head
        head = nn
        n = n.next
    return head

def solution2(head):

    # reversed_ll = rec_reverse(head)
    # return compare(head,reversed_ll.head)
    reversed_ll_head = iter_reverse(head)
    return compare(head,reversed_ll_head)

def compare(h1, h2):

    while h1 and h2:
        if h1.data != h2.data:
            return False
        h1, h2 = (h1.next, h2.next)
    return True


def createLL(ll):

    head = Node(ll[0])
    node = head
    for n in ll[1:]:
        node.next = Node(n)
        node = node.next

    return head

def printLL(head):
    node = head
    while node != None:
        print(node.data,end='->')
        node = node.next
    print()

if __name__ == '__main__':
    print("Enter numbers representing Linked Lists: (e.g. '0 1 2 1 0' )")
    ll = list(map(int,input().split()))
    h1 = createLL(ll)

    printLL(h1)
    print("Is the LL a Palindrome: {}".format(solution1(h1)))

    print("Is the LL a Palindrome: {}".format(solution2(h1)))