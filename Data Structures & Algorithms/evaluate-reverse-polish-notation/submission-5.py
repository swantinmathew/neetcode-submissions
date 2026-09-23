class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in "+-/*":
                stack.append(int(tokens[i]))
            elif tokens[i]=="+":
                a=stack.pop()
                b=stack.pop()
                result =  b+a
                stack.append(result)  
            elif tokens[i]=="-":
                a=stack.pop()
                b=stack.pop()
                result =  b-a
                stack.append(result)
            elif tokens[i]=="*":
                a=stack.pop()
                b=stack.pop()
                result =  b*a
                stack.append(result) 
            elif tokens[i]=="/":
                a=stack.pop()
                b=stack.pop()
                result =  int(b/a)
                stack.append(result)    
        return int(stack[0]);                 