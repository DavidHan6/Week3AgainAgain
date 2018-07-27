x = input("What do you want in the list")
class MyQueue:
    my_list = []
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_list = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.my_list.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.my_list) > 0:
            popped = self.my_list[0]
            self.my_list = self.my_list[1:]
            print(popped)
            return popped

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.my_list) > 0:
            YEET = self.my_list[0]
            print(YEET)
            return YEET

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.my_list) == 0:
            return True


#Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
