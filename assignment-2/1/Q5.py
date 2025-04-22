queue = []
while True:
    action = input("Enter 'add' to add an item, 'remove' to remove an item, or 'quit' to exit: ")
    if action == 'add':
        item = input("Enter the item to add: ")
        queue.append(item)
    elif action == 'remove':
        if queue:
            print("Removed:", queue.pop(0))
        else:
            print("Queue is empty.")
    elif action == 'quit':
        break