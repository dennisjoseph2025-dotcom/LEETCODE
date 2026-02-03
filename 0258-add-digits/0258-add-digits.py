class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        x = sum(int(a) for a in str(num))
        return self.addDigits(x)