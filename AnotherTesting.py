class MyStack:
    def __init__(self):
        self.list = []
    def push(self, x):
        self.list.append(x)
    def pop(self):
        # obj = MyQueue()
        # obj1 = MyQueue1()
        # i = 0
        # while (i < len(obj.list)):
        #     obj1.push(obj.pop(obj.list[i]))
        if (len(self.list) == 0):
            return "Error 404: Not Found"
        i = 0
        ii = self.list[-1]
        list = []
        while (i < len(self.list)-1):
            list.append(self.list[i])
            i+=1
        self.list=list
        return ii
    def top(self):
        if (len(self.list) != 0):
            return self.list[-1]
        else:
            return "Error 404: Not Found"
    def empty(self):
        return (len(self.list) == 0)
    # def poli(self, x):
    #     if (len(self.list) > x):
    #         return "Error: Input is less than list"
    #     else:
    #         i = 0
    #         ii = self.list[-x]
    #         li = []
    #         while (i < len(self.list) - len(x)):
    #             li.append(self.list[i])
    #             i+=1
    #         self.list = li
    #         return ii
    def pushli(self, x):
        self.list = self.list + x

class MyStack1:
    def __init__(self):
        self.list = []
    def push(self, x):
        self.list.append(x)
    def pop(self):
        # obj = MyQueue()
        # obj1 = MyQueue1()
        # i = 0
        # while (i < len(obj.list)):
        #     obj1.push(obj.pop(obj.list[i]))
        if (len(self.list) == 0):
            return "Error 404: Not Found"
        i = 0
        ii = self.list[-1]
        list = []
        while (i < len(self.list)-1):
            list.append(self.list[i])
            i+=1
        self.list=list
        return ii
    def top(self):
        if (len(self.list) != 0):
            return self.list[-1]
        else:
            return "Error 404: Not Found"
    def empty(self):
        return (len(self.list) == 0)
    # def poli(self, x):
    #     if (len(self.list) > x):
    #         return "Error: Input is less than list"
    #     else:
    #         i = 0
    #         ii = self.list[-x]
    #         li = []
    #         while (i < len(self.list) - len(x)):
    #             li.append(self.list[i])
    #             i+=1
    #         self.list = li
    #         return ii
    def pushli(self, x):
        self.list = self.list + x


class MyQueue:
    # list = []
    def __init__ (self):
        self.list = []
    def push(self, x):
        self.list.append(x)
    def pop(self):
        obj = MyStack()
        obj1 = MyStack1()
        # obj.push(1)
        # obj.push(10)
        # obj.push(111)
        # obj.push(1010)
        i = 0
        ii = obj.list[0]
        print(obj.list)
        print(obj1.list)
        z = len(obj.list)
        if (z == 0):
            return "Error 404: List is Empty"
        while (i < z):
            obj1.push(obj.pop())
            print(obj.list)
            print(obj1.list)
        # return obj1.list
            i+=1
        # if (len(self.list) == 0):
        #     return "Error 404: Not Found"
        # i = 1
        # ii= self.list[0]
        # list = []
        # while (i < len(self.list)):
        #     list.append(self.list[i])
        #     i+=1
        # self.list=list
        ii = obj1.pop()
        print(obj.list)
        print(obj1.list)
        while (i > 1):
            obj.push(obj1.pop())
            print(obj.list)
            print(obj1.list)
        # return obj1.list
            i-=1
        return ii
    def pop1(self):
        obj = MyStack()
        obj1 = MyStack1()
        # obj1.push(1)
        # obj1.push(10)
        # obj1.push(111)
        # obj1.push(1010)
        i = 0
        ii = obj1.list[0]
        print(obj.list)
        print(obj1.list)
        z = len(obj1.list)
        if (z == 0):
            return "Error 404: List is Empty"
        while (i < z):
            obj.push(obj1.pop())
            print(obj.list)
            print(obj1.list)
        # return obj1.list
            i+=1
        # if (len(self.list) == 0):
        #     return "Error 404: Not Found"
        # i = 1
        # ii= self.list[0]
        # list = []
        # while (i < len(self.list)):
        #     list.append(self.list[i])
        #     i+=1
        # self.list=list
        ii = obj.pop()
        print(obj.list)
        print(obj1.list)
        while (i > 1):
            obj1.push(obj.pop())
            print(obj.list)
            print(obj1.list)
        # return obj1.list
            i-=1
        return ii
    def peek(self):
        #return list[0]
        if (len(self.list) != 0):
            return self.list[0]
        else:
            return "Error 404: Not Found"
    def empty(self):
        return (len(self.list) == 0)
    def poli(self, x):
        if (len(self.list) < x):
            return "Error: Input is larger than list"
        else:
            i = x
            ii = self.list[0:x]
            li = []
            while (i < len(self.list)):
                li.append(self.list[i])
                i+=1
            self.list=li
            return ii
    def pushli(self, x):
        self.list = self.list + x

i = MyQueue()
ii = MyStack1()
# ii.push(1)
# print(ii.list)
# ii.pop()
# print(ii.list)
print(i.pop1())
# print(ii.list)
