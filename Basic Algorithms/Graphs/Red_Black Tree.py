'''
Red-Black Tree Insertion
1. If tree is empty create a new node as a root, color is black
2. If tree is not empty create new node as a leaf, color is red

3. If parent of new node is black, exit
4. If parent of new node is red:
    - if parent's sibling is black or "Nil": rotate and recolor
    - if parent's sibling is red: recolor.
      If parent's parent is not root: recolor it and check its parent
=====================================================================
RULES
* root -> black
* no two adjacent red nodes
* count number of black nodes same in each path

'''
