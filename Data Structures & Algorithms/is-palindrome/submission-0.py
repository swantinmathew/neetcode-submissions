class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for char in s:
            if char.isalnum():
                newstr+=char.lower()
        l = len(newstr)
        for i in range(l//2):
            if newstr[i]!=newstr[l-i-1]:
                return False
        return True        
