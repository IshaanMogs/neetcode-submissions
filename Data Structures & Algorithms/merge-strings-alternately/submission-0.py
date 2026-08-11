class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = ""
        f = 0
        s = 0
        i=0
        while f<len(word1) and s<len(word2):
            if i%2==0:
                merged+=word1[f]
                f+=1
            else:
                merged+=word2[s]
                s+=1
            i+=1
        while len(word1)>f:
            merged+=word1[f]
            f+=1
        while len(word2)>s:
            merged+=word2[s]
            s+=1
        return merged
