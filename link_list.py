class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class Slist:
    def __init__(self):
        self.headval = None

    def printlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


s_list = Slist()
s_list.headval = Node(1)
e2 = Node('x')
e3 = Node(2)
e4 = Node('x')
e5 = Node(3)
s_list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5

s_list.printlist()
