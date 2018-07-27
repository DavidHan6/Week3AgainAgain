x = input("What do you want in the list")
class MyStack:
    List = []
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.List = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.List.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.List) > 0:
            popped = self.List[0]
            self.List = self.List[1:]
            print(popped)
            return popped

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.List) > 0:
            YEET = self.List[-1]
            print(YEET)
            return YEET


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.List) == 0:
            return True


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
