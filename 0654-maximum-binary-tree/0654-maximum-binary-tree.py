# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return 
        
        res = TreeNode(max(nums))

        mid = nums.index(max(nums))

        res.left = self.constructMaximumBinaryTree(nums[:mid])
        res.right = self.constructMaximumBinaryTree(nums[mid+1:])
        return res



