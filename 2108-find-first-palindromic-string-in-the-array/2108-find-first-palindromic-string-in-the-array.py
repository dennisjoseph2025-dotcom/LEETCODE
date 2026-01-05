class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        p=[]
        for x in words:
            np=[]
            for y in x:
                np.append(y)
            np.reverse()
            
            if list(x) == np:
                p.append("".join(x))
        if len(p)==0:
            return ""
        else:
            return p[0]             