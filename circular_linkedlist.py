class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class CircularLinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this circular linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
            if item == self.tail:
                ll_str += f'HEAD ({item.next}) ->'
                return ll_str
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            if node.next == self.head:
                return items
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        """=> O(1) because this is a comparison of a known value"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        """=> O(n) because we must traverse the length of n elements of the list to get a count"""
        """Even if n=1 this is technically still O(n) because O(1) represents constant time"""
        count = 0
        if self.head:
            current_node = self.head
            count += 1
            while current_node.next != self.head:
                count += 1
                current_node = current_node.next
        return count

        # TODO: Loop through all nodes and count one for each

    def add(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        """=> O(1) because self.tail is tracked, and we are appending one item to a known location"""
        # TODO: Create new node to hold given item
        node = Node(item)
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty() == True:
            self.head = node 
            self.tail = self.head
        # TODO: Else append node after tail
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head

    def find(self, matcher):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        => O(1) best case if the item being found is the first item in the list
        TODO: Worst case running time: O(???) Why and under what conditions?
        => O(n) worst case if the item being found is the last item in the list"""

        node = self.head
        while node:
            if matcher in node.data:
                return True
            if node.next == self.head:
                break
            node = node.next
        return False

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        => O(1) best case if item being deleted is the first item in the list
        TODO: Worst case running time: O(???) Why and under what conditions?
        => O(n) worst case if the item being deleted is the last item in the list"""
        # TODO: Loop through all nodes to find one whose data matches given item
        previous_node = None
        next_node = None
        if self.head:
            current_node = self.head
            while item != current_node.data: # loop until data is found
                if current_node.next == None:
                    raise ValueError('Item not found: {}'.format(item))
                else:
                    previous_node = current_node
                    current_node = current_node.next
                    if current_node.next:
                        next_node = current_node.next
                    else:
                        self.tail = current_node
            if current_node == self.head: # if data is found in the head
                if current_node.next != self.head:
                    # if there is more than one node then current node will not he referencing itself
                    # set new head node to the to-be-deleted head node's.next node
                    self.head = current_node.next
                    # set the tail's .next node to the new head
                    self.tail.next = self.head
                else:
                    # if there is only one node
                    self.head = None
                    self.tail = None
                    self = None
            elif current_node.next == None: # if data is found in the tail
                # set the new tail to be the previous node
                self.tail = previous_node
                # remove the forward link from the node being removed
                current_node.next = None
                # remove the .next link leading to the node being removed and point that at the head instead
                self.tail.next = self.head   
            else: # data is found between head and tail
                if current_node.next:
                    previous_node.next = current_node.next
                    current_node.next = None
                else:
                    self.tail = previous_node
                    self.tail.next = self.head
        else:
            raise ValueError('Item not found: {}'.format(item))

    # TODO: Update previous node to skip around node with matching data
    # TODO: Otherwise raise error to tell user that delete has failed
    # Hint: raise ValueError('Item not found: {}'.format(item))

    def replace(self, match, replacement):
        node = self.head
        while node:
            if match == node.data:
                node.data = replacement
            node = node.next
        
def test_circular_linked_list():
    cll = CircularLinkedList()
    print(cll)
    print('\nTesting add:')
    for item in ['A', 'B', 'C']:
        print('add({!r})'.format(item))
        cll.add(item)
        print('list: {}'.format(cll))

    print('head: {}'.format(cll.head))
    print('tail: {}'.format(cll.tail))
    print('length: {}'.format(cll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            cll.delete(item)
            print('list: {}'.format(cll))
        print('head: {}'.format(cll.head))
        print('tail: {}'.format(cll.tail))
        print('length: {}'.format(cll.length()))

if __name__ == '__main__':
    test_circular_linked_list()

