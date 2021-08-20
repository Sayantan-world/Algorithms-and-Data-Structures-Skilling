class StringStack:
    def __init__(self):
        self.stack = []
    
    def printStack(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            tempStack = self.stack[::-1]
            for string in tempStack:
                print(string)
    
    def pushOp(self,s):
        if len(self.stack) >= 10:
            print("Stack is full")
        else:
            self.stack.append(s)
    
    def popOp(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            self.stack.pop()

def solution(pushN,popN,stringList):
    # Write your code here...
    s = StringStack()
    
    for string in stringList:
        s.pushOp(string)
    
    s.printStack()
    
    while popN:
        s.popOp()
        popN -= 1
    
    s.printStack()
    
pushN = int(input())
popN = int(input())
stringList = []
for i in range(pushN):
    stringList.append(input())
solution(pushN,popN,stringList)