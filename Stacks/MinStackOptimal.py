class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        if len(self.stack) == 0 and len(self.min_stack) == 0:
            self.min_stack.append(x)
        elif len(self.min_stack) != 0 and x <= self.min_stack[-1]:
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.min_stack) != 0 and len(self.stack) !=0 and self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
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
        return self.min_stack[-1] if len(self.min_stack) !=0 else None


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   #--> Returns -3.
minStack.pop()
print(minStack.top())      #--> Returns 0.
print(minStack.getMin())   #--> Returns -2.