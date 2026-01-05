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
# Exercise 3
    def check_palindrome(self):
        start=self.head
        end=self.tail
        while start and start.next:
            if start.data!=end.data:
                return False
            if start==end or start.next==end:#checked till half so palindrome
                return True            
            start=start.next
            end=end.prev




a=DoublyLinkedList()
a.insert_first(50)
a.insert_first(20)
a.insert_first(30)
a.insert_first(20)
a.insert_first(50)
a.print_list()
print("Is it a palindrome?", a.check_palindrome())
print()
b=DoublyLinkedList()
b.insert_first(50)
b.insert_first(20)
b.insert_first(20)
b.insert_first(50)
b.print_list()
print("Is it a palindrome?", b.check_palindrome())

print()
c=DoublyLinkedList()
c.insert_first('a')
c.insert_first('c')
c.insert_first('c')
c.insert_first('b')
c.insert_first('a')
c.print_list()
print("Is it a palindrome?", c.check_palindrome())