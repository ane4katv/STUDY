class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2

        node = TreeNode(nums[mid])

        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        print(node.val)
        return node


tree = Solution()
array = [2,3,4]

tree.sortedArrayToBST(array)

# for i in tree.list_for_bst(array):
#     tree.insert(tree.root, i)

# tree.insert(tree.root, 3)
# tree.insert(tree.root, 7)
# tree.insert(tree.root, 2)
# tree.insert(tree.root, 4)
# tree.insert(tree.root, 6)
# tree.insert(tree.root, 8)

