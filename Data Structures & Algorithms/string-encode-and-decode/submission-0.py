class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for w in strs:
            i = str(len(w))
            s += i+"#"+w
        return s
    def decode(self, s: str) -> List[str]:
        i=0
        word=[]
        while i<len(s):
            length=""
            while s[i]!="#":
                length+=s[i]
                i+=1
            length = int(length)
            word.append(s[i+1:i+1+length])
            i=i+1+length
        return word
