class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_val):
        self.root = Node(root_val)
    # Inserting new values into the tree
    def insert(self, value):
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.val:
            if current_node.left is None:
                current_node.left = Node(value) 
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.val:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)
    # In-Order Traversal --> (left --> root --> right)
    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.val)
            self.inorder_traversal(node.right, result)
    
    # Pre Order Traversal (root --> left --> right)
    def preorder_traversal(self, node, result):
        if node:
            result.append(node.val)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    # Post Order Traversal (left --> right --> root)
    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.val)

    # Search for a value in a Tree
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if current_node.val == value:
            return True
        elif value < current_node.val:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)
    

# Example
if __name__ == "__main__":
    tree = BinaryTree(10)

    # Insert Values
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)
    tree.insert(12)
    tree.insert(18)

    # In Order Traversal
    result = []
    tree.inorder_traversal(tree.root, result)
    print("Inorder Traversal: ", result)

    # Pre Order Traversal
    result = []
    tree.preorder_traversal(tree.root, result)
    print("Preorder Traversal: ", result)

    # Post Order Traversal
    result = []
    tree.postorder_traversal(tree.root, result)
    print("Postorder Traversal: ", result)

    # Search for a value
    print("Is 7 in the tree?", tree.search(7))
    print("Is 20 in the tree?", tree.search(20))