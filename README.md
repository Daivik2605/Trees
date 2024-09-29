# Tree Data Structures

This repository contains important concepts and implementations related to tree data structures in Python. Below are the various types of trees, along with a brief explanation of each type.

---

# Types of Trees in Data Structures

## 1. General Tree
A **general tree** is the most basic type of tree. In a general tree, each node can have any number of child nodes. There is no restriction on the number of children a node can have.

## 2. Binary Tree
A **binary tree** is a type of tree in which each node has at most two children. These two children are usually referred to as the **left child** and **right child**. Binary trees are widely used due to their simple structure and easy implementation.

- **Full Binary Tree**: A binary tree in which every node other than the leaf nodes has two children.
- **Complete Binary Tree**: A binary tree where all levels are fully filled except possibly the last, and all nodes are as far left as possible.
- **Perfect Binary Tree**: A binary tree in which all interior nodes have two children and all leaf nodes are at the same level.
- **Degenerate (or Pathological) Binary Tree**: A binary tree where each parent node has only one child, making it essentially a linked list.

#### Binary Tree Implementation in Python

This repository contains an implementation of a **Binary Tree** in Python. The code defines a `Node` class and a `BinaryTree` class that supports various tree operations such as insertion, searching, and traversal.

#### Features

- **Node class**: Represents a node in the binary tree, holding the value and pointers to its left and right children.
- **BinaryTree class**: 
  - Allows for inserting new values into the tree.
  - Supports searching for a value in the tree.
  - Provides different tree traversal methods: 
    - **In-order Traversal**
    - **Pre-order Traversal**
    - **Post-order Traversal**

#### Traversals

##### In-order Traversal (Left, Root, Right)
- Visits the left subtree first, then the root node, and finally the right subtree.
- This traversal returns the values in ascending order if the tree is a Binary Search Tree (BST).

##### Pre-order Traversal (Root, Left, Right)
- Visits the root node first, followed by the left subtree, and then the right subtree.


##### Post-order Traversal (Left, Right, Root)
- Visits the left subtree first, followed by the right subtree, and finally the root node.

#### Search Operation

The tree also supports a search function to find whether a specific value exists in the tree. The search function performs recursively, starting from the root node and traversing down the tree.


## 3. Binary Search Tree (BST)
A **binary search tree** is a binary tree with an additional property: for every node, the values in its left subtree are less than the node’s value, and the values in its right subtree are greater than the node’s value. This property makes searching operations faster, making BSTs a common choice for searching tasks.

## 4. Balanced Tree
A **balanced tree** is a tree where the height of the left and right subtrees of any node differ by at most one. Balanced trees ensure that operations like insertion, deletion, and searching have time complexity close to O(log n).

- **AVL Tree**: A type of self-balancing binary search tree where the difference between the heights of left and right subtrees is at most one for every node. AVL trees automatically balance themselves after every insertion or deletion.
- **Red-Black Tree**: A self-balancing binary search tree where each node has an extra bit for denoting the color of the node, either red or black. The tree ensures that no two consecutive red nodes appear on any path from the root to a leaf and that the number of black nodes is the same on all paths from the root to the leaves.

## 5. Heap
A **heap** is a special tree-based data structure that satisfies the heap property. It is used primarily for priority queue operations. There are two main types of heaps:
- **Max-Heap**: In a max-heap, the key at a parent node is always greater than or equal to the keys of its children.
- **Min-Heap**: In a min-heap, the key at a parent node is always less than or equal to the keys of its children.

## 6. B-Tree
A **B-tree** is a self-balancing search tree in which nodes can have more than two children. B-trees are commonly used in databases and file systems because they can minimize disk access during searches. B-trees are a generalization of binary search trees in that a node can have multiple children.

## 7. Trie (Prefix Tree)
A **trie**, also known as a **prefix tree**, is a tree data structure commonly used for storing strings. In a trie, each node represents a single character of a string, and the path from the root to a leaf represents a full string. Tries are particularly useful for operations like searching for words in dictionaries and autocomplete systems.

## 8. Suffix Tree
A **suffix tree** is a compressed trie of all suffixes of a given string. This tree allows fast pattern matching and substring searching, making it particularly useful in bioinformatics and text processing.

## 9. Segment Tree
A **segment tree** is a binary tree used for storing intervals or segments. It allows querying which segments contain a certain point or updating which intervals contain that point. This type of tree is useful for answering range queries efficiently.

## 10. Fenwick Tree (Binary Indexed Tree)
A **Fenwick Tree**, also called a **Binary Indexed Tree (BIT)**, is a data structure that provides efficient methods for calculation and manipulation of prefix sums. It is used to perform both point updates and prefix queries in O(log n) time.

---
## 112 - Path Sum Problem

### Problem Description

The Path Sum problem involves determining whether a binary tree has a root-to-leaf path such that the sum of the node values along the path equals a given `targetSum`. A leaf is a node with no children.

### Example

- **Input**: `root = [5,4,8,11,null,13,4,7,2,null,null,null,1]`, `targetSum = 22`
- **Output**: `True`
- **Explanation**: The path 5 -> 4 -> 11 -> 2 sums up to 22.

### Note

Feel free to check out the [code implementation](./112-pathsum.py) and try it yourself!


---

## How to Use This Repository

Each type of tree will have its own folder in this repository, containing the Python implementation and code examples of various operations such as insertion, deletion, traversal, and searching.

Stay tuned for updates and code examples!

---

