"""
Time Complexity:
    Access (Getting/Setting an element): O(n) - Similar to singly linked lists, accessing an element in the worst case requires traversing the list from the beginning or end depending on how close the element is to either side.
    Search: O(n) - Just like singly linked lists, searching for a specific element might involve iterating through all nodes in the list.
    Insertion:
        Beginning/End: O(1) - Due to the presence of both previous and next pointers in each node, inserting at the beginning or end involves modifying a constant number of pointers.
        Arbitrary position: O(1) - With access to both previous and next pointers, insertion at any position only requires updating the pointers of the surrounding nodes, making it a constant time operation.
    Deletion:
        Beginning/End: O(1) - Similar to insertion, removing from the beginning or end involves updating a constant number of pointers thanks to the double links.
        Arbitrary position: O(1) - Once you have the node to delete, its previous and next pointers can be swiftly adjusted, resulting in constant time deletion.

Space Complexity:
    Space: O(n) - Each node in the doubly linked list stores data, a pointer to the next node, and a pointer to the previous node. This additional pointer compared to singly linked lists leads to a space complexity of O(n), still linear with respect to the number of elements.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next_pointer = None
        self.previous_pointer = None
    
class SLL:
    def __init__(self):
        self.head_pointer = None
        self.tail_pointer = None

    def append(self, node):
        if self.head_pointer is None:
            self.head_pointer = node
            self.tail_pointer = node
            return
        self.tail_pointer.next_pointer = node
        node.previous_pointer = self.tail_pointer
        self.tail_pointer = node
        return
    
    def pop(self):
        popped_value = self.tail_pointer.value
        self.tail_pointer = self.tail_pointer.previous_pointer
        self.tail_pointer.next_pointer = None
        return popped_value
    
    def display(self):
        if self.head_pointer is None:
            print('Empty Linked List')
            return
        traversal_pointer = self.head_pointer
        while traversal_pointer.next_pointer:
            print(str(traversal_pointer.value) + ' -> ', end='')
            traversal_pointer = traversal_pointer.next_pointer
        print(traversal_pointer.value)

    def display_reverse(self):
        if self.tail_pointer is None:
            print('Empty Linked List')
            return
        traversal_pointer = self.tail_pointer
        while traversal_pointer.previous_pointer:
            print(str(traversal_pointer.value) + ' -> ', end='')
            traversal_pointer = traversal_pointer.previous_pointer
        print(traversal_pointer.value)


if __name__=='__main__':
    single_linked_list = SLL()
    single_linked_list.append(Node(1))
    single_linked_list.append(Node(2))
    single_linked_list.append(Node(3))
    single_linked_list.append(Node(4))
    single_linked_list.display()
    single_linked_list.display_reverse()
    print(single_linked_list.pop())
    single_linked_list.display()
    single_linked_list.display_reverse()