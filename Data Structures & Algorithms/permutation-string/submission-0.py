class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen={}
        saw={}
        for i in range(len(s1)):
            if s1[i] in seen:
                seen[s1[i]]+=1
            else:
                seen[s1[i]]=1   
        left=0
        for right in range(len(s2)):
            if s2[right] in saw:
                saw[s2[right]]+=1
            else:
                saw[s2[right]]=1
            if right-left+1==len(s1):
                if saw==seen:
                    return True                            
                saw[s2[left]] -=1
                if saw[s2[left]]==0:
                    del saw[s2[left]]
                left+=1
        return False    