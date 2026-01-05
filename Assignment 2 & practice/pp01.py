stack = []

def is_empty():
    return len(stack) == 0

def enstack(x):
        stack.append(x)

def destack():
    if is_empty():
        print("stack underflow")
    else:
        print(f"Destackd: {stack.pop()}")

def display():
    if is_empty():
        print("stack is empty")
    else:
        print("stack elements:", ' '.join(map(str, stack)))

def print_front_and_rear():
    if is_empty():
        print("stack is empty")
    else:
        print(f"Front element: {stack[0]}")
        print(f"Rear element: {stack[-1]}")
def clear_stack():
    while not is_empty():
        destack()
def reverse_string(string):
    new=""
    clear_stack()
    list= string.split(" ")
    for i in list:
        for j in i:
            enstack(j)
        while not is_empty():
            new+=stack.pop()
        new+=" "
    print(new)
    

def menu():
    while True:
        print("\n!!!  MENU  !!!")
        print("1. Enstack")
        print("2. Destack")
        print("3. Display")
        print("4. Print Front and Rear")
        print("6. Reverse word wise String")
        print("5. Quit")
        
        option = input("Select an option: ")

        if option == '1':
            data = int(input("Enter data to enstack: "))
            enstack(data)
        elif option == '2':
            destack()
        elif option == '3':
            display()
        elif option == '4':
            print_front_and_rear()
        elif option == '5':
            break
        elif option =="6":
            string=input("Enter the string to reverse using stack")
            reverse_string(string)
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    menu()

