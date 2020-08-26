'''
Author: Goog Tech
Date: 2020-08-26 14:12:49
LastEditTime: 2020-08-26 14:13:28
Description: https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/
FilePath: \leetcode-googtech\#448. Find All Numbers Disappeared in an Array\Solution.py
WebSite: https://algorithm.show/
'''

class Solution(object):

    # 原地修改法
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 初始化结果列表
        result = []
        # 循环遍历数组元素
        for i in range(len(nums)):
            # 将 nums[i] - 1 索引位置的元素标记为负数
            # 先获取当前元素的绝对值,然后 -1 进而将当前元素转换为 nums 数组的索引值
            newIndex = abs(nums[i]) - 1
            # 若该索引值在数组 nums 中存在,则将其所指的元素变为负数
            if nums[newIndex] > 0:
                nums[newIndex] *= -1
        # 再次遍历数组,若当前数组元素 nums[i] 为负数,则说明在数组中存在数字: i + 1
        # 反之则说明数组中缺失的数字为: i + 1
        for i in range(0, len(nums)):
            # 将缺失的数字添加到结果列表中
            if nums[i] > 0: result.append(i + 1)
        # 返回结果列表
        return result
