from linkedlist import LinkedList

def detect_cycle(ll):
    # two pointers move at different speeds, one slow, one fast
    slow_current = ll.head
    fast_current = ll.head
    while fast_current:
        # increment both pointers by one
        slow_current = slow_current.next
        fast_current = fast_current.next
        # increment fast pointer again if there are more nodes
        # if we hit None then there is no loop
        if fast_current:
            fast_current = fast_current.next
        if slow_current == fast_current:
            return True
    # exit condition is to return False if no cycle in ll
    return False

# non-cycling linked list setup
ll = LinkedList()
ll.append(1)
ll.append(3)
ll.append(5)
ll.append(7)

# cycling linked list setup
print(detect_cycle(ll))
cll = LinkedList()
cll.append(1)
cll.append(3)
cll.append(5)
cll.append(7)
cll.tail.next = cll.head.next

print(detect_cycle(cll)) 



