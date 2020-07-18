'''
@Author: Goog Tech
@Date: 2020-07-18 22:10:48
@Description: https://leetcode-cn.com/problems/middle-of-the-linked-list/
@FilePath: \leetcode-googtech\#876. Middle of the Linked List\Solution.py
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 快指针fastNode每次走2步,慢指针slowNode每次走1步,
        # 当fastNode走到末尾时slowNode正好走到中间
        fastNode = slowNode = head
        while fastNode and fastNode.next:
            fastNode = fastNode.next.next
            slowNode = slowNode.next
        return slowNode
