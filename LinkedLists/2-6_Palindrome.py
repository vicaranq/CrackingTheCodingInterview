'''
    2.6 Implement a function to check if a linked list is a palindrome
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def solution1(head):
    ''' Implementing an iterative approach to find where the middle is using a slow and fast pivot. I create a stack
    and append values while iterating to half of the list. Then, I start checking top of the stack with next element of
     slow. Check is done for the ODD case. '''
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
    # get sum
    print("Is the LL a Palindrome: {}".format(solution1(h1)))