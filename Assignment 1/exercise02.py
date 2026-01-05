# Md Mainul Islam
# 0152430008
# Sec: BA 
# DSA I Lab , Spring 25

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        print("Linked list: ", end="")
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("NULL")
# Exercise 2
    def delete_duplicate(self):# for sorted LL only
        current=self.head
        while current and current.next:
            while current.next and current.data==current.next.data:
                current.next=current.next.next
            current=current.next
        return self    
    
a=LinkedList()
a.insert_first(50)
a.insert_first(40)
a.insert_first(30)
a.insert_first(20)
a.insert_first(10)
print("Before:")
a.print_list()
print("After Removing Duplicates:")
a.delete_duplicate().print_list()
b=LinkedList()
b.insert_first(30)
b.insert_first(30)
b.insert_first(20)
b.insert_first(20)
b.insert_first(10)
b.insert_first(10)
print()
print("Before:")
b.print_list()
print("After Removing Duplicates:")
b.delete_duplicate().print_list()
# c=LinkedList()
# c.insert_first(20)
# c.insert_first(20)
# c.insert_first(10)
# c.insert_first(10)
# c.insert_first(10)
# c.insert_first(10)
# print()
# print("Before:")
# c.print_list()
# print("After Removing Duplicates:")
# c.delete_duplicate().print_list()