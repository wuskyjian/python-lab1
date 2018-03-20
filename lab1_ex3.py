#  Exercise 3

print("""
Insert the number corresponding to the action you want to perform: 

   1. insert a new task; 
   2. remove a task; 
   3. show all the tasks; 
   4. close the program. 
   
Your choice:""")

choice = '-1'
task = []

while True:
    choice = input()
    if choice == '1':
        print("Please enter one task: ")
        task_insert = input()
        task.append(task_insert)
        print("Task:\"", task_insert, "\"is inserted.")
        print("Your choice:")
    elif choice == '2':
        print("Please enter the task you want to remove: ")
        task_removed = input()
        task.remove(task_removed)
        print("Task:\"", task_removed, "\"is removed.")
        print("Your choice:")
    elif choice == '3':
        print("The whole task list is:", task)
        print("Your choice:")
    elif choice == '4':
        print("Program closed.")
        break
    else:
        print("""
        Wrong input, please follow the input rules
        
        1. insert a new task; 
        2. remove a task; 
        3. show all the tasks; 
        4. close the program. 
        
        Your choice:""")
