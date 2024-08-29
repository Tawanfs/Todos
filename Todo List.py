from functions import get_todos, write_todos

while True:
    choose = input("Type Add, Edit, Show, Complete or Exit. ").strip()
    
    if choose.startswith(("add", "new")):
        try:
            todo = choose.split(maxsplit=1)[1]
            todos = get_todos()

            todos.append(todo + '\n')
            todos = [item.title() for item in todos]

            write_todos(todos)
        except (ValueError, IndexError):
            input("Please type a todo...")
            continue

    elif "show" in choose:

        todos = get_todos()
        new = [print(f"{i+1}-{item.strip()}") for i, item in enumerate(todos)]

    elif choose.startswith("edit"):
        try:
            number = int(choose.split(maxsplit=1)[1]) - 1
        
            todos = get_todos()
        
            new = input("Replace the todo: ") + '\n'
            new = new.title()

            print(f"'{todos[number].strip()}' was replaced by '{new.strip()}'")
            todos[number] = new

            todos = write_todos(todos)
        except ValueError:
            print("Your comand is not valid")
            continue
                

    elif choose.startswith("complete"):
        try:
            todos = get_todos()
            
            number = int(choose.split(maxsplit=1)[1])
            number = number - 1
            print(todos[number].strip('\n'), 'was completed.')
            todos.pop(number)

            todos = write_todos(todos)
        except IndexError:
            print("This number is not in the range")
            continue
    elif "exit" in choose:
        break
    else:
        print("Please insert a existing option...")
