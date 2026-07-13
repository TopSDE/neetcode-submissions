class Solution:

    def encode(self, arr: List[str]) -> str:
        temp = []   
        for word in arr:
            temp.append(str(len(word)) + ":" + word)
            
        return ''.join(temp)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
    
            while s[j+1] != ':':
                j += 1
    
            res.append(s[j+2 : j+2+int(s[i : j+1])])
            i = j+2+int(s[i : j+1])
    
        return res