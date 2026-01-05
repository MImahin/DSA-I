class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)
        self.top += 1

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return -1
        self.top -= 1
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print("Empty Stack")
            return -1
        return self.stack[self.top]

    def display(self):
        if self.isEmpty():
            print("Empty Stack")
            return
        print("Stack elements:", ' '.join(map(str, reversed(self.stack))))

def menu():
    stack = Stack()

    while True:
        print("\n!!!  MENU  !!!")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Quit")
        option = int(input("Select an option: "))

        if option == 1:
            data = int(input("Enter data to push: "))
            stack.push(data)
        elif option == 2:
            data = stack.pop()
            if data != -1:
                print(f"Popped element: {data}")
        elif option == 3:
            data = stack.peek()
            if data != -1:
                print(f"Top element: {data}")
        elif option == 4:
            stack.display()
        elif option == 5:
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    menu()
