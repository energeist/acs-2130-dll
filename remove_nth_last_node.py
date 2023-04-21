from linkedlist import LinkedList

def remove_nth_last_node(linked_list, n):
    # initialize current_node as the head of the linked list
    current_node = linked_list.head
    length = linked_list.length()
    # iterate over linked list while counter value is greater than 1 
    # head node is n=1 and doesn't need to be double counted
    while length > n:
        current_node = current_node.next
        length -= 1
    linked_list.delete(current_node.data)
    return linked_list

ll = LinkedList()
ll.append(1)
ll.append(3)
ll.append(5)
ll.append(7)
ll.append(9)

print(ll) # (1) -> (3) -> (5) -> (7) -> (9) -> || (7) should be removed if n = 2
print(remove_nth_last_node(ll, 2)) # (1) -> (3) -> (5) -> (9) ->

# I have chosen to use the built in linkedlist methods.  Note that it would be more 
# computationally efficient to manipulate nodes directly.