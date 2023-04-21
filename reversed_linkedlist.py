from linkedlist import LinkedList

def reverse_ll(forward_list):
    # assume that as a final product we only want one list and set of nodes remaining (not None)
    reversed_list = LinkedList()
    # append the head of the forward list to a new reversed linked list
    reversed_list.append(forward_list.head.data)
    # initialize current_node pointer
    current_node = forward_list.head
    while current_node:
        # set the next_node pointer
        next_node = current_node.next
        # set current_node reference from original list to None
        current_node = None
        if next_node:
            # prepend the next_node's data to a list in a new node, if it exists
            reversed_list.prepend(next_node.data)
        # reset current_node pointer for next iteration
        current_node = next_node
    # remove reference to the original list
    forward_list = None
    return reversed_list

def reverse_ll_in_place(ll):
    # code to reverse linked list in place
    # iterate over list and prepend each node back on the list
    current_node = ll.head
    while current_node:
        # head node doesn't need to be manipulated
        if current_node == ll.head:
            current_node = current_node.next
            ll.head.next = None
        ll.prepend(current_node.data)
        current_node = current_node.next
    return ll
        
        
forward_ll = LinkedList()
forward_ll.append(1)
forward_ll.append(2)
forward_ll.append(3)
reverse_in_place = reverse_ll_in_place(forward_ll)
# reversed_ll = reverse_ll(forward_ll)
print(f"Forward linked list: {forward_ll}")
# print(f"Reversed linked list: {reversed_ll}")
print(f"Reversed linked list: {reverse_in_place}")

        