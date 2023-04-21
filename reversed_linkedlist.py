from linkedlist import Node
from linkedlist import LinkedList

def reverse_ll(forward_list):
    reversed_list = LinkedList()
    # append the head of the forward list to a new reversed linked list
    reversed_list.append(forward_list.head.data)
    current_node = forward_list.head
    while current_node is not None:
        current_node = current_node.next
        if current_node is not None:
            reversed_list.prepend(current_node.data)
    return reversed_list

forward_ll = LinkedList()
forward_ll.append(1)
forward_ll.append(2)
forward_ll.append(3)
reversed_ll = reverse_ll(forward_ll)
print(f"Forward linked list: {forward_ll}")
print(f"Reversed linked list: {reversed_ll}")
        