class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        ans = dict()
        for i in s:
            ans[i] = ans.get(i,0)+1
        for i in t:
            if i not in ans or ans[i]==0:
                return False
            ans[i]-=1
        return True