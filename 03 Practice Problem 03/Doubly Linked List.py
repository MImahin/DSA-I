class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
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
            new_node.prev = current

    def insert_at(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        current_position = 0
        while current and current_position < position - 1:
            current = current.next
            current_position += 1

        if current is None:
            print("Position is out of bounds!")
        else:
            new_node.next = current.next
            new_node.prev = current

            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node

    def delete_first(self):
        if self.head is None:
            print("List is empty. Cannot delete the first node.")
            return
        temp = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        del temp

    def delete_last(self):
        if self.head is None:
            print("List is empty. Cannot delete the last node.")
            return
        elif self.head.next is None:
            del self.head
            self.head = None
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.prev.next = None
            del current

    def delete_item(self, item):
        current = self.head
        while current:
            if current.data == item:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                del current
                return
            current = current.next
        print("Item not found. Node not deleted.")

    def print_forward(self):
        current = self.head
        print("Doubly linked list (forward):", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")

    def print_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        print("Doubly linked list (backward): NULL", end=" ")
        while current:
            print("<- ", current.data, end=" ")
            current = current.prev
        print()


def menu():
    doubly_linked_list = DoublyLinkedList()

    while True:
        print("\nMenu:")
        print("1. Insert First")
        print("2. Insert Last")
        print("3. Insert At")
        print("4. Delete First")
        print("5. Delete Last")
        print("6. Delete Item")
        print("7. Print the list (forward)")
        print("8. Print the list (backward)")
        print("9. Quit")
        option = int(input("Select an option: "))

        if option == 1:
            data = int(input("Enter data to insert at the beginning: "))
            doubly_linked_list.insert_first(data)
        elif option == 2:
            data = int(input("Enter data to insert at the end: "))
            doubly_linked_list.insert_last(data)
        elif option == 3:
            data = int(input("Enter data to insert: "))
            position = int(input("Enter position to insert at: "))
            doubly_linked_list.insert_at(data, position)
        elif option == 4:
            doubly_linked_list.delete_first()
        elif option == 5:
            doubly_linked_list.delete_last()
        elif option == 6:
            item = int(input("Enter the item to delete: "))
            doubly_linked_list.delete_item(item)
        elif option == 7:
            doubly_linked_list.print_forward()
        elif option == 8:
            doubly_linked_list.print_backward()
        elif option == 9:
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    menu()
