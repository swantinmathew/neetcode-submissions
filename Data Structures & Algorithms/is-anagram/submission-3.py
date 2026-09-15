class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs={}
        freqt={}
        for char in s:
            if char in freqs:
                freqs[char] = freqs[char]+1
            else:
                freqs[char] = 1    

        for char in t:
            if char in freqt:
                freqt[char] = freqt[char]+1
            else:
                freqt[char] = 1    

        if freqs==freqt:
            return True
        else:
            return False            
                
                