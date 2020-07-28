'''
@Author: Goog Tech
@Date: 2020-07-28 21:54:41
@Description: https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/
@FilePath: \leetcode-googtech\#102. Binary Tree Level Order Traversal\559.n叉树的最大深度.py
'''

#
# @lc app=leetcode.cn id=559 lang=python
#
# [559] N叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    # 递归法
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # 判断根节点是否为空或无孩子节点
        if not root: return 0
        if not root.children: return 1
        # 初始化最大深度值及当前子树的深度值
        maxDepth = currentDepth = 0
        # 遍历当前节点的子节点,即求出当前子树的深度值
        for child in root.children:
            currentDepth = self.maxDepth(child)
            # 判断当前子树的深度是否为最大深度值
            maxDepth = currentDepth if currentDepth > maxDepth else maxDepth
        # 一棵树的最大深度值就是子树最大深度值加一
        return maxDepth + 1


# @lc code=end
