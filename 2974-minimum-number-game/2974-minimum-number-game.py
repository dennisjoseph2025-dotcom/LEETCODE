class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=0
        b=0
        arr=[]
        for i in range(0, len(nums), 2):
            a=min(nums)
            nums.remove(a)
            b=min(nums)
            nums.remove(b)
            arr.append(b)
            arr.append(a)
        return arr    