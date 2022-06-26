class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

class Graph:
    graph = {
        1: [2,3,None],
        2: [4,None],
        3: [None],
        4: [5,6,None],
        5: [6,None],
        6: [None]
    }