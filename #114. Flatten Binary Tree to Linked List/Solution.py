'''
Author: Goog Tech
Date: 2020-09-27 17:47:41
LastEditTime: 2020-09-27 17:49:59
Description: https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
FilePath: \leetcode-googtech\#114. Flatten Binary Tree to Linked List\Solution.py
WebSite: https://algorithm.show/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # 递归解法
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 判断根节点及其左右子树是否为空
        if not root or (not root.left and not root.right):
            return root
        # 将左右子树捋直
        self.flatten(root.left)
        self.flatten(root.right)
        # 将捋直的右子树备份一下
        tempTree = root.right
        # 将捋直的左子树放置到右边
        root.right = root.left
        # 将左子树置空
        root.left = None
        # 找到现右子树中的最后一个节点
        while(root.right):
            root = root.right
        # 将捋直的原来的右子树接到现右子树的右子树上
        root.right = tempTree
