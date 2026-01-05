# Md Mainul Islam
# 0152430008
# Sec: BA 
# DSA I Lab , Spring 25

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail=new_node
    def print_list(self):
        current = self.head
        print("Linked list: ", end="")
        while current:
            print(f"{current.data} <-> ", end="")
            current = current.next
        print("NULL")

# Exercise 4
    def bubble_sort(self):
        if self.head==None or self.tail==None:
            return self
        end=self.tail
        flag=True
        while flag:
            start=self.head
            flag=False
            while start is not end:
                if start.data>start.next.data:
                    start.data,start.next.data=start.next.data,start.data
                    flag=True
                start=start.next
            end.prev=end
        
        return self
    

a=DoublyLinkedList()
a.insert_first(3)
a.insert_first(1)
a.insert_first(5)
a.insert_first(2)
a.insert_first(4)
a.print_list()
print("After Sorting")
a.bubble_sort().print_list()
