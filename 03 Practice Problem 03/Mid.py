class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def insert_first(self, head, data):
        new_node = Node(data)
        new_node.next = head
        head = new_node

    def find_mid(self,head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def print_list(self,head):
        current = head
        print("Linked list: ", end="")
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("NULL")

    def detect_cycle(self,head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def menu():
    linked_list = LinkedList()
    
    head = Node(1)
    first = Node(2)
    second = Node(3)
    third = Node(4)

    head.next = first
    first.next = second
    second.next = third
    third.next = first


    while True:
        print("\n!!! MENU !!!")
        print("1. Insert First")
        print("2. Print the list")
        print("3. Find Mid")
        print("4. Detect Cycle")
        print("5. Quit")

        option = int(input("Select an option: "))

        if option == 1:
            data = int(input("Enter data to insert at the beginning: "))
            linked_list.insert_first(head, data)
        elif option == 2:
            linked_list.print_list(head)
        elif option == 3:
            mid = linked_list.find_mid(head)
            print("Mid: ", mid)
        elif option == 4:
            flag = linked_list.detect_cycle(head)
            if flag == True:
                print("Cycle Exists")
            else:
                print("No Cycle")
        elif option == 5:
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    menu()