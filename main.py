from DoublyLinkedList import DoublyLinkedList

# Example:  12 ↔️ 200 ↔️ 19 ↔️ 49

dll = DoublyLinkedList()
dll.append(10)
print(dll.head.data)
dll.append(12)
print(dll.head.next.data)
dll.append(200)
print(dll.head.next.next.data)
print(dll.head.next.next.previous.data)
print(dll.find(12))
print(dll.update(12, 24))
print(dll.find(24))
dll.append(19)
dll.append(49)
print(dll.find(200))
print(dll.remove(200))
print("trying to find 200")
print(dll.find(200))
print(dll.insert(25,24))