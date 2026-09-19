class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        seen={}
        maxfreq=0
        res=0
        for r in range(len(s)):
            if s[r] in seen:
                seen[s[r]]+=1
            else:
                seen[s[r]]=1
            maxfreq=max(maxfreq,seen[s[r]])    
            while (r-l+1)-maxfreq>k:
                seen[s[l]]-=1
                l+=1
            res = max(res,r-l+1)    
        return res    
