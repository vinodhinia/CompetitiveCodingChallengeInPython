import sys
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = sys.maxsize

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0: return None
        temp_Stack = []
        self.min = sys.maxsize
        while len(self.stack) != 0:
            temp = self.stack.pop()
            self.min = min(temp, self.min)
            temp_Stack.append(temp)
        while len(temp_Stack) != 0:
            self.stack.append(temp_Stack[-1])
            temp_Stack.pop()
        return self.min

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   #--> Returns -3.
minStack.pop()
print(minStack.top())      #--> Returns 0.
print(minStack.getMin())   #--> Returns -2.
