import FreeSimpleGUI as sg
from functions import get_todos, write_todos

todos = get_todos() 

label = sg.Text("Insert a Todo:")
input = sg.InputText(tooltip="Type a Todo", key="todo")
add = sg.Button("ADD")
exit = sg.Button("EXIT")
edit = sg.Button("EDIT")
box = sg.Listbox(todos, key="todos", justification='center', size=(20,10),expand_y=True)
complete = sg.Button("COMPLETE")
layout = [[label],[input, add],[box, edit],[complete],[exit]], 

window = sg.Window("My Todo App",layout=layout,
                    font=('Arial', 15)
)
while True:
    event, values = window.Read()
    
    if event == "ADD":
        new_todo = values["todo"]
        new_todo = new_todo.title()
        todos.append(new_todo + '\n')
        write_todos(todos)
        
        window['todos'].update(values=todos)
    
    elif event == "EDIT":
        selected = values["todos"][0]
        new_todo = values["todo"]  
        index = todos.index(selected)
        todos[index] = new_todo.title() + '\n'
        write_todos(todos) 
        
        window['todos'].update(values=todos)
        
    elif event == "COMPLETE":
        selected = values["todos"][0]
        index = todos.index(selected)
        todos.pop(index)
        write_todos(todos)
        
        window['todos'].update(values=todos)
       
    elif event == "EXIT" or event == sg.WINDOW_CLOSED:
        break
    
        
       