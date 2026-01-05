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
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    menu()
