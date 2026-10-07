# length prefix encoding is the best way so we can store length+str simply

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s))+':'+s

        return result
        ## 5:hello5:code

    def decode(self, s: str) -> List[str]:
        i = 0 
        res = []
        while i<len(s):
            j = i 
            while s[j]!=':':
                j+=1
            length = int(s[i:j])
            j+=1
            res.append(s[j:j+length])
            i = length + j
        return res









