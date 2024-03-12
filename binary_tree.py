"""
Time Complexity:
    Access: O(h) - In a balanced binary tree, access (finding a specific node) involves traversing down the tree following comparisons at each level. The height (h) of the tree determines the number of comparisons, leading to a time complexity of O(h).
    Search: O(h) - Similar to access, searching for a particular element also involves traversing the tree based on comparisons at each level. In a balanced tree, this has a time complexity of O(h).
    Insertion: O(h) - Inserting a new node involves traversing the tree to find the appropriate position based on the binary search tree property (left child < parent < right child). This traversal takes O(h) time in a balanced tree.
    Deletion: O(h) - Deleting a node also requires navigating the tree to locate the target node and then potentially rearranging the tree structure. In a balanced tree, this has a time complexity of O(h).

Space Complexity:
    Space: O(n) - In the worst case scenario, a binary tree can become skewed (all nodes lean to one side), resembling a linked list. This unbalanced tree requires space proportional to the number of elements (O(n)). However, in a balanced binary tree, the space complexity is typically considered O(n) as well, due to the efficient use of space with most nodes having two children.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left_pointer = None
        self.right_pointer = None

class BTree:
    def __init__(self):
        self.root_node = None
    
    def append(self, value):
        self.root_node = self._append(value, self.root_node)

    def _append(self, value, traversal_root):
        if traversal_root is None:
            return Node(value)
        else:
            if value<traversal_root.value:
                traversal_root.left_pointer = self._append(value, traversal_root.left_pointer)
            else:
                traversal_root.right_pointer = self._append(value, traversal_root.right_pointer)
        return traversal_root
        
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root_node, result)
        return result

    def _inorder_traversal(self, traversal_root, result):
        if traversal_root:
            self._inorder_traversal(traversal_root.left_pointer, result)
            result.append(traversal_root.value)
            self._inorder_traversal(traversal_root.right_pointer, result)
    
    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root_node, result)
        return result

    def _preorder_traversal(self, traversal_root, result):
        if traversal_root:
            result.append(traversal_root.value)
            self._preorder_traversal(traversal_root.left_pointer, result)
            self._preorder_traversal(traversal_root.right_pointer, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root_node, result)
        return result

    def _postorder_traversal(self, traversal_root, result):
        if traversal_root:
            self._postorder_traversal(traversal_root.left_pointer, result)
            self._postorder_traversal(traversal_root.right_pointer, result)
            result.append(traversal_root.value)

if __name__=='__main__':
    tree = BTree()
    tree.append(3)
    tree.append(2)
    tree.append(1)
    tree.append(4)
    tree.append(5)
    print(tree.inorder_traversal())
    print(tree.preorder_traversal())
    print(tree.postorder_traversal())