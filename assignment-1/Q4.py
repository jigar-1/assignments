name = input("Enter your name: ")
response = ("That is a nice name" if name == "Alice" else
            "How you dare!" if name in ["John Cleese", "Michael Palin"] else
            "You have a nice name.")
print(response)