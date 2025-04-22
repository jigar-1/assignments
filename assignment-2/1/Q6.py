stack = []
while True:
    action = input("Enter 'push' to add an item, 'pop' to remove an item, or 'quit' to exit: ")
    if action == 'push':
        item = input("Enter the item to push: ")
        stack.append(item)
    elif action == 'pop':
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty.")
    elif action == 'quit':
        break