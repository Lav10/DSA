"""
Time Complexity:
    Access (Getting/Setting an element): O(n) - In the worst case, you need to traverse the entire list from the head to reach a specific element.
    Search: O(n) - Similar to access, searching for a particular element might require iterating through all nodes in the list.
    Insertion:
        Beginning: O(1) - Adding a new node at the beginning only involves modifying the head pointer.
        End: O(n) - In the absence of a tail pointer, finding the last node for insertion requires traversing the entire list.
        Arbitrary position: O(n) - Inserting in the middle depends on finding the node before the desired position, which again takes O(n) time.
    Deletion:
        Beginning: O(1) - Similar to insertion at the beginning, removing the head node involves updating the head pointer.
        End: O(n) - Requires finding the node before the one to be deleted, which has a complexity of O(n).
        Arbitrary position: O(n) - Deleting from the middle necessitates finding the node before the target node, leading to O(n) complexity.

Space Complexity:
    Space: O(n) - Each node in the linked list stores data and a pointer to the next node, resulting in linear space usage proportional to the number of elements.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next_pointer = None
    
class SLL:
    def __init__(self):
        self.head_pointer = None

    def append(self, node):
        if self.head_pointer is None:
            self.head_pointer = node
            return
        traversal_pointer = self.head_pointer
        while traversal_pointer.next_pointer:
            traversal_pointer = traversal_pointer.next_pointer
        traversal_pointer.next_pointer = node
        return
    
    def pop(self):
        traversal_pointer = self.head_pointer
        while traversal_pointer.next_pointer.next_pointer:
            traversal_pointer = traversal_pointer.next_pointer
        popped_value = traversal_pointer.next_pointer.value
        traversal_pointer.next_pointer = None
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

if __name__=='__main__':
    single_linked_list = SLL()
    single_linked_list.append(Node(1))
    single_linked_list.append(Node(2))
    single_linked_list.append(Node(3))
    single_linked_list.display()
    print(single_linked_list.pop())
    single_linked_list.display()