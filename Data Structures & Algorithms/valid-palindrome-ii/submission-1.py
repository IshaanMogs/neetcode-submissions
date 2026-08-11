class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s)-1
        def check(s,l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        while left<right:
            if s[left]!=s[right]:
                return check(s,left+1,right) or check(s,left,right-1)
            if s[left]==s[right]:
                left+=1
                right-=1 
        return True