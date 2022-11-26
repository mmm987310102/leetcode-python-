'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。



'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #先创建一个字典把列表存起来
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        #在新字典找对应的和为目标的两个值
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)#得到j的index
            if j is not None and i != j:
                return [i, j]
