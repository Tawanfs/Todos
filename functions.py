from datetime import date

def get_time():
   today = date.today()
   return today

date = str(f"{get_time()}.txt")

def get_todos(filepath=date):
    """ Read a text file and return the list of to-do items
    """
    with open(filepath, 'r') as file:
            todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=date):
    """ Write the todos items in a text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
try:
    get_todos()
except FileNotFoundError:
    write_todos("")

   
    
   
        
        
       