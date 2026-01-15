class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b=[]
        c=0
        y=0
        for x in nums:
            if 0<len(b):
                c=b[y-1] +x
                b.append(c)
            else:
                b.append(nums[0])
            y+=1

        return b