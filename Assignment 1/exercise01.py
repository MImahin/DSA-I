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


# excercise 1
def merge_and_sort(sll1,sll2):
    current=sll1.head
    if current:
        while current.next:
            current=current.next
        current.next=sll2.head
    else:
        sll1=sll2
    current=sll1.head
    flag=True
    while flag:
        current2=sll1.head
        flag=False
        while current2 and current2.next:
            if current2.data>current2.next.data:
                current2.data,current2.next.data=current2.next.data,current2.data
                flag=True
            current2=current2.next
    return sll1
print("LL 01")
a=LinkedList()
a.insert_first(80)
a.insert_first(50)
a.insert_first(20)
a.insert_first(10)
a.insert_first(30)
a.print_list()
print("LL 02")
b=LinkedList()
b.insert_first(40)
b.insert_first(100)
b.insert_first(60)
b.insert_first(90)
b.insert_first(70)
b.print_list()
c=merge_and_sort(a,b)
print("Output : LL01,LL02")
c.print_list()
print()


d=LinkedList()
e=LinkedList()
d.insert_first(20)
d.insert_first(10)
d.insert_first(30)
e.insert_first(20)
e.insert_first(10)
e.insert_first(30)
print("LL 03")
d.print_list()
print("LL 04")
e.print_list()
f=merge_and_sort(d,e)
print("Output : LL03,LL04")
f.print_list()