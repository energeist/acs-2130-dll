from Node import Node

class DoublyLinkedList:
  
    def __init__(self):
        self.head = None
        self.tail = None

    # TODO: append()
    #Add to the end of the linked list
    def append(self, new_data):
        if self.head is None:#empty linked list
            new_node = Node(new_data)
            self.head = new_node
            self.tail = new_node
        else:
            #create a new node
            new_node = Node(new_data)
            #set new node previous to tail
            new_node.previous = self.tail
            #set tail.next to new node
            self.tail.next = new_node
            #move tail to new node
            self.tail = new_node

    # TODO: insert()
    def insert(self, item, index):
        current_node = self.head
        while current_node:
            if current_node.data == index:
                new_node = Node(item)
                new_node.next = current_node.next
                new_node.previous = current_node
                current_node.next.previous = new_node
                current_node.next = new_node
                return f"inserted node with data {item} after node with {current_node.data} and before node with {new_node.next.data}"
            else:
                current_node = current_node.next
        raise ValueError

    # TODO: remove()
    def remove(self, value):
        current_node = self.head
        while current_node:
            print(current_node.data)
            if current_node.data == value:
                current_node.previous.next = current_node.next
                current_node.next.previous = current_node.previous
                return f"Deleted node with data {value}"
            elif current_node.next == None:
                raise ValueError    
            else:
                current_node = current_node.next
        

  # TODO: update()
  #Find and existing node with data == item and update with new value
  #traverse to find node
  #replace the data with value
  #hint: look at find() for singly linked list
    def update(self, item, value):
        current_node = self.head
        while current_node:
            if current_node.data == item:
                current_node.data = value
                return f"updated node with data {item} to {value}"   
            else:
                current_node = current_node.next
        raise ValueError

  # TODO: find()
    def find(self, item):
        current_node = self.head
        while current_node:
            if current_node.data == item:
                return f"found {item}"
            else:
                current_node = current_node.next
        return False        