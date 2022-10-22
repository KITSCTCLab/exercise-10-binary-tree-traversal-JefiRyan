# Problem 

Given an array of integers, construct binary tree and print inorder, preorder and postorder traversals.

Implement the following functions:
> **insert(root, new_value) -> BinaryTreeNode:** 
* If binary search tree is empty, make a new node, declare it as root and return the root.</br>
* If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.</br>
* If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.</br>
* Finally, return the root.</br>
> **inorder(root) -> None** : 
* Print inorder traversal.</br>
> **preorder(root) -> None** : 
* Print preorder traversal.</br>
> **postorder(root) -> None** : 
* Print postorder traversal.</br>

        
# Constraints
* The number of the nodes in the tree is in the range [0, 100].
* -100 <= data <= 100

## Sample Input - 1
```
15, -10, 25, -6, 14, -20, 60
```
## Sample Output - 1
```
-20 -10 -6 14 15 25 60 
15 -10 -20 -6 14 25 60 
-20 14 -6 -10 60 25 15
```
<b><i>Explanation<i></b></br>
Construct the binary tree using the given input.</br>
First line of output represents inorder traversal.</br>
Second line of output represents preorder traversal.</br>
Third line of output represents postorder traversal.</br>

## Sample Input - 2
```
15, 10, 25, 6, 14, 20, 60
```
## Sample Output - 2
```
6 10 14 15 20 25 60 
15 10 6 14 25 20 60 
6 14 10 20 60 25 15
```
