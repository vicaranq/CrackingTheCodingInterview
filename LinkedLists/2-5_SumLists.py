'''
Question: You have two numbers represented by a linked list where each node contains a single digit. The digits are
stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers
 and returns the sum as a linked list.

Example:
    Input: 7 1 6
           5 9 2
    Output:2 1 9

FOLLOW UP:
Suppose that the digits are stored in forward order. Repeat above problem

Example:
    Input: 6 1 7
           2 9 5
    Output:9 1 2

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def solution(h1, h2):

    head_sum = Node(-1)
    prev = head_sum
    carry = 0
    while h1 or h2:
        if h1 and h2:
            sum = h1.data + h2.data
        elif h2:
            sum = h2.data
        else:
            sum = h1.data

        # get result digit and carry
        r = sum % 10 + carry
        carry = sum // 10

        prev.next = Node(r)
        prev = prev.next

        if h1 and h2:
            h1, h2 = (h1.next, h2.next)
        elif h2:
            h2 = h2.next
        else:
            h1 = h1.next

    if carry:
        prev.next = Node(carry)
    return head_sum.next

def solution2(h1, h2):

    head_sum = Node(-1)
    carry = 0
    solution2_helper(h1, h2, head_sum, carry)
    return head_sum.next

def solution2_helper(h1, h2, prev_node, carry):

    if not h1 and not h2 and not carry:
        return None

    sum = 0
    sum += h1.data if h1 else 0
    sum += h2.data if h2 else 0
    sum += carry if carry else 0

    # get result digit and carry
    r = sum % 10
    carry = sum // 10

    prev_node.next = Node(r)

    if h1 and h2:
        solution2_helper(h1.next, h2.next, prev_node.next, carry)
    elif h2:
        solution2_helper(None, h2.next, prev_node.next, carry)
    elif h1:
        solution2_helper(h1.next, None, prev_node.next, carry)

def ll_len(head):

    count = 0
    while head != None:
        count += 1
        head = head.next
    return count

def pad(head,count):
    # pad front of LL with zeros

    while count > 0:
        n = Node(0)
        n.next = head
        head = n
        count -= 1
    return head

def solution_followup(h1, h2):

    len1 = ll_len(h1)
    len2 = ll_len(h2)

    if len1 < len2:
        h1 = pad(h1, len2-len1)
    elif len1 > len2:
        h2 = pad(h2, len1-len2)

    # printLL(h1)
    # printLL(h2)
    (carry, head) = folloup_helper(h1, h2)

    if carry:
        n = Node(carry)
        n.next = head
        head = n
    return head

def folloup_helper(h1, h2):

    if not h1 and not h2:
        return (0, None)

    sum = 0
    sum += h1.data if h1 else 0
    sum += h2.data if h2 else 0

    if h1 and h2:
        data_store = folloup_helper(h1.next, h2.next)
    elif h2:
        data_store = folloup_helper(None, h2.next)
    else:
        data_store = folloup_helper(h1.next, None)

    prev_carry = data_store[0]
    prev_digit_object = data_store[1]

    r = sum % 10 + prev_carry
    carry = sum // 10

    n = Node(r)
    n.next = prev_digit_object

    return (carry, n)




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
    # print("Enter numbers representing Linked Lists: (e.g. '7 1 6' and '5 9 2')")
    # ll = list(map(int,input().split()))
    # ll2 = list(map(int,input().split()))
    # h1 = createLL(ll)
    # h2 = createLL(ll2)
    #
    # printLL(h1)
    # printLL(h2)
    #
    # # get sum
    # sum_head = solution2(h1,h2)
    # printLL(sum_head)

    # --- Follow Up ---
    print("\nFOLLOW UP:\nEnter numbers representing theLinked List: (e.g. '6 1 7')\nLL1:")
    ll = list(map(int,input().split()))
    print("LL2:")
    ll2 = list(map(int,input().split()))
    h1 = createLL(ll)
    h2 = createLL(ll2)

    printLL(h1)
    printLL(h2)

    # get sum
    sum_head = solution_followup(h1,h2)
    print("Output:")
    printLL(sum_head)