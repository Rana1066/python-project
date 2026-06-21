tasks =[
    'wake up',
    'go to gym',
    'breakfast'
]
isCont = True
# def addTask()
#     return


while isCont:
    options=input("Select option 1 for Add task, 2 for Remove Task, 3 for Show Task list ");

    if(options == '1'):
        addTask=input("Enter the task ")
        tasks.append(addTask)
    if(options == '2'):
        for task in tasks:
            print(tasks.index(task),task)
        removeTask=input('Enter task id to remove ')
            # print(removeTask)
            # tasks.remove(removeTask)
            # print(task)
    if(options == '3'):
        for task in tasks:
            print(task)
    print('do you want to cont..')
    isCont=input('Y or N')
    if isCont == 'n':
        break
