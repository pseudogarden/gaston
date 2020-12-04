class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in nums:
            for y in nums:
                if nums.index(y) != nums.index(x):
                    if target - y == x:
                        return [nums.index(x), nums.index(y)]
        
    print(twoSum([3,3,5,6,1], 4))