todo_list = []

# Добавяме задачи към графика
def add_task(task):
    todo_list.append(task)
    print('Task added successfully')

# Премахваме задачи от графика
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print('Task removed successfully')
    else:
        print('Task not found in the list.')

# Показва ниу всички задачи
def vie_task():
    if todo_list:
        print('Tasks: ')
        for task in todo_list:
            print(task)
    # Ако листа е празен и нямаме задачи
    else:
        print('No tasks in the To Do list.')

while True:
    print('\n---To-Do List App---')
    print('1. Add task')
    print('2. Remove task')
    print('3. View task')
    print('4. Exit')

    choice = input('Enter your choice(1-4):')

    if choice == '1':
        task = input('Enter task:')
        add_task(task)

    elif choice == '2':
        task = input('Enter task to remove: ')
        remove_task(task)

    elif choice == '3':
        vie_task()

    elif choice == '4':
        print('Exiting the program!')
        break

    else:
        print('Invalid choice. Please try agan!')




