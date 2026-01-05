class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res=""
        for i in words:
            a=i[::-1]
            if  res == "":
                if a == i:
                    res=i
        return res
        