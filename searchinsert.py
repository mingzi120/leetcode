class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        for num in nums:
            if num >= target:
                if target != num:
                    nums.insert(nums.index(num),target)
                    return nums.index(num)-1
                else:
                    return nums.index(num)
        nums.insert(len(nums),target)
        return len(nums)-1


s=Solution()
s.searchInsert([1,3,5,6],7)