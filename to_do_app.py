todos = []

print("Welcome to your to-do list app.")

def add(todo):
    todos.append(todo)
    print(f"Your todo list includes:")
    for index, todo in enumerate(todos):
        print(f"{index + 1}. {todo}")

def remove():
    print("Below is your available todo")
    for index, todo in enumerate(todos):
        print(f"{index + 1}. {todo}")
    edit = int(input("Enter todo number to remove: "))
    todos.pop(edit - 1)
    print(f"Your todo after edit is:")
    for index, todo in enumerate(todos):
        print(f"{index + 1}. {todo}")

def complete():
    done = int(input("Enter the completed todo: "))
    todos.pop(done - 1)
    print(f"Your remaining todo is:")
    for index, todo in enumerate(todos):
        print(f"{index + 1}. {todo}")

def show():
    print("This is what you have in your todo list:")
    for index, todo in enumerate(todos):
        print(f"{index + 1}. {todo}")


while True:
    print("What would you like to do:")
    options = ["Add", "Remove", "Complete", "show", "quit"]
    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")
    to_do = input("Enter here: ")

    if to_do == "1":
        user = input("Enter todo: ")
        add(user)
    elif to_do == "2":
        remove()
    elif to_do == "3":
        complete()
    elif to_do == "4":
        show()
    elif to_do == "5":
        print("That is all for now.")
        break
    else:
        print("Please enter a valid option")