from copy import deepcopy


class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)
        new_node.link = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.link:
                current = current.link
            current.link = new_node

    def insert_at(self, data, position):
        if position < 0:
            print("Invalid position.")
            return
        elif position == 0:
            self.insert_first(data)
            return
        else:
            new_node = Node(data)
            current = self.head
            current_position = 0
            while current and current_position < position - 1:
                current = current.link
                current_position += 1
            if current is None:
                print("Position exceeds the length of the list. Node not inserted.")
                return
            else:
                new_node.link = current.link
                current.link = new_node

    def delete_first(self):
        if self.head is None:
            print("The list is empty. Nothing to delete.")
            return
        else:
            temp = self.head
            self.head = self.head.link
            del temp

    def delete_last(self):
        if self.head is None:
            print("The list is empty. Nothing to delete.")
            return
        elif self.head.link is None:
            del self.head
            self.head = None
            return
        else:
            current = self.head
            while current.link and current.link.link:
                current = current.link
            del current.link
            current.link = None

    def delete_item(self, item):
        current = self.head
        prev = None
        while current:
            if current.data == item:
                if prev:
                    prev.link = current.link
                else:
                    self.head = current.link
                del current
                return
            else:
                prev = current
                current = current.link
        print("Item not found. Node not deleted.")

    def search_item(self, item):
        current = self.head
        position = 0
        while current:
            if current.data == item:
                return position
            current = current.link
            position += 1
        return -1

    def print_list(self):
        current = self.head
        print("Linked list: ", end="")
        while current:
            print(f"{current.data} -> ", end="")
            current = current.link
        print("NULL")
    def print_size(self):
        if self.head==None:
            print("0")
        else :
            current=self.head
            size=1
            while current.link:
                size+=1
                current=current.link
            print(size)
    def mid(self):
        slow=self.head
        fast=self.head
        while fast.link and fast.link.link:
            slow=slow.link
            fast=fast.link.link
        print(slow.data)
        return slow
    def check_occurence(self,data):
        count=0
        current=self.head
        data=int(data)
        while current:
            if current.data==data:
                count+=1
            current=current.link
        print(count)
    def sorted_insert(self,data):
        
        if self.head==None or data<=self.head.data:
            self.insert_first(data)
            return
        current=self.head
        while current.link and data>current.link.data:
            current=current.link
        new=Node(data)
        new.link=current.link
        current.link=new
    def del_even(self):
        current=self.head
        prev=None
        while current:
            if current.data%2==0:
                if prev is not None:
                    prev.link=current.link
                    del current
                    current= prev.link
                    continue
                temp=current.link
                del current
                current= temp 
                self.head=current
                continue
            prev=current
            current=current.link
    def reverse(self):
        current=self.head
        prev=None
        while current:
            temp=current.link
            current.link=prev
            prev=current
            current=temp
        if prev is not None:
            self.head=prev
        return self
    def rotate(self,k):
        count=0
        current=self.head
        while current and count<k:
            count+=1
            data=current.data
            current=current.link
            self.delete_first()
            self.insert_last(data)
            current
    def palindrome(self):
        if not self.head or not self.head.link :
            return False
        current=deepcopy(self)
        current.reverse()
        first=self.mid()
        second=current.mid()
        while second and first:
            if second.data != first.data:
                return False
            first=first.link
            second=second.link
        return True
    def cycle(self):
        slow=self.head
        fast=self.head
        while fast and fast.link:
            slow=slow.link
            fast=fast.link.link
            if slow==fast:
                return True
        return False
    def make_cycle(self):
        if not self.head or not self.head.link :
            print("Not Possible")
            return 
        current=self.head
        while current.link:
            current=current.link
        current.link=self.head
        





# Menu-based interface
def menu():
    linked_list = LinkedList()

    while True:
        print("\n!!! MENU !!!")
        print("1. Insert First")
        print("2. Insert Last")
        print("3. Insert At")
        print("4. Delete First")
        print("5. Delete Last")
        print("6. Delete Item")
        print("7. Print the list")
        print("8. Search")
        print("9. Quit")
        print("10. Print Size ")
        print("11. Demo LL ")
        print("12. Mid")
        print("13. Check Occurence")
        print("14. Sorted Insert")
        print("15. Delete Even")
        print("16. Reverse")
        print("17. Rotate by K")
        print("18. It's a Palindrome!!")
        print("19. It's a Cycle!!")
        print("20. Make it a Cycle")

        option = int(input("Select an option: "))

        if option == 1:
            data = int(input("Enter data to insert at the beginning: "))
            linked_list.insert_first(data)
        elif option == 2:
            data = int(input("Enter data to insert at the end: "))
            linked_list.insert_last(data)
        elif option == 3:
            data = int(input("Enter data to insert: "))
            position = int(input("Enter position to insert at: "))
            linked_list.insert_at(data, position)
        elif option == 4:
            linked_list.delete_first()
        elif option == 5:
            linked_list.delete_last()
        elif option == 6:
            item = int(input("Enter the item to delete: "))
            linked_list.delete_item(item)
        elif option == 7:
            linked_list.print_list()
        elif option == 8:
            item = int(input("Enter the item to search: "))
            position = linked_list.search_item(item)
            if position != -1:
                print(f"Item found at position {position}.")
            else:
                print("Item not found in the list.")
        elif option == 9:
            break
        elif option == 10:
            linked_list.print_size()
        elif option == 11:
            List=[1,2,3,4,5,6,7,8,9]
            for i in List:
                linked_list.insert_last(i) 
            linked_list.print_list()
        elif option == 12:
            linked_list.mid()
        elif option == 13:
            data=input("Enter the Value to check occureence: ")
            linked_list.check_occurence(data)
        elif option == 14:
            data=int(input("Enter Value to insert: "))
            linked_list.sorted_insert(data)
        elif option == 15:
            linked_list.del_even()
        elif option == 16:
            linked_list.reverse()
        elif option == 17:
            k=int(input("Enter K to rotate by that term: "))
            linked_list.rotate(k)
        elif option == 18:
            print(linked_list.palindrome())
        elif option == 19:
            print(linked_list.cycle())
        elif option == 20:
            linked_list.make_cycle()

        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    menu()
