queue = []

def is_empty():
    return len(queue) == 0

def enqueue(x):
        queue.append(x)

def dequeue():
    if is_empty():
        print("Queue underflow")
    else:
        print(f"Dequeued: {queue.pop()}")

def display():
    if is_empty():
        print("Queue is empty")
    else:
        print("Queue elements:", ' '.join(map(str, queue)))

def print_front_and_rear():
    if is_empty():
        print("Queue is empty")
    else:
        print(f"Front element: {queue[0]}")
        print(f"Rear element: {queue[-1]}")

def menu():
    while True:
        print("\n!!!  MENU  !!!")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Print Front and Rear")
        print("5. Quit")
        option = input("Select an option: ")

        if option == '1':
            data = int(input("Enter data to enqueue: "))
            enqueue(data)
        elif option == '2':
            dequeue()
        elif option == '3':
            display()
        elif option == '4':
            print_front_and_rear()
        elif option == '5':
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    menu()

