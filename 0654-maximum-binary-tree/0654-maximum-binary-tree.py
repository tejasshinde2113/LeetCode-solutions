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

        llist = nums[:mid]
        rlist = nums[mid+1:]

    


        res.left = self.constructMaximumBinaryTree(llist)
        res.right = self.constructMaximumBinaryTree(rlist)
        return res



        # def dfs(left,right):
        #     print(left, right)
        #     if len(left)<2 or not right:
        #         return

        #     mid = left.pop()
        #     res = TreeNode(mid)

        #     lmid = left.index(max(left))
        #     rmid = right.index(max(right))
        #     res.left = dfs(left[:lmid+1],left[lmid+1:])
        #     res.right = dfs(right[:rmid],right[rmid+1:])
        #     return res
        # mid = nums.index(max(nums))
        # return dfs(nums[:mid+1],nums[mid+1:])
        