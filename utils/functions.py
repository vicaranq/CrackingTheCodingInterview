import classes

def printLL(head):
    node = head
    while node != None:
        print(node.data,end='->')
        node = node.next
    print()
