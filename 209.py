```
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        plus=0
        right=0
        min_length=float('inf')
        for left in range(len(nums)):
            while right<len(nums) and plus<s:
                plus=plus+nums[right]
                right=right+1
            if plus>=s:
                min_length=min(min_length, right-left)#前面已经加过一了
            plus=plus-nums[left]
        if min_length==float('inf'):
            return 0
        return min_length


```
