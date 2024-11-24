# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
           return 
        arr =[]
        while head:
            arr.append(head.val)
            head = head.next
        

        def f(l,r):
            if l>r:
                return None

            m = (l+r)//2
            root = TreeNode(arr[m])
            root.left = f(l,m-1)
            root.right = f(m+1,r)

            return root
        
        return (f(0,len(arr)-1))
        
        

