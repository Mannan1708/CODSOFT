import os
import json

todo_file = 'todo.json'
def display(task):
    if not task:
        print("No task found.")
    else:
        for index, task in enumerate(task, start=1):
            status = "Done" if task['done'] else "Not Done"
            print(f"{index}. {task['task']} - {status}")
def add(task):
    desc = input("Enter the task ")
    task.append({"task": desc, "done": False})
    save(task)
    print("Added successfully.")            
def update(task):
    display(task)
    try:
        index = int(input("To update enter a task number ")) - 1
        if 0 <= index < len(task):
            task[index]['task'] = input("Enter new task ")
            save(task)
            print("Updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid task number.")
def done(task):
    display(task)
    try:
        index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= index < len(task):
            task[index]['done'] = True
            save(task)
            print("Task done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid task number.")
def delete(task):
    display(task)
    try:
        index = int(input("To delete enter task number ")) - 1
        if 0 <= index < len(task):
            task.pop(index)
            save(task)
            print("Deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid task number.")
def upload():
    if os.path.exists(todo_file):
        with open(todo_file, 'r') as file:
            return json.load(file)
    return []
def save(task):
    with open(todo_file, 'w') as file:
        json.dump(task, file, indent=4)
def main():
    task = upload()
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display(task)
        elif choice == '2':
            add(task)
        elif choice == '3':
            update(task)
        elif choice == '4':
            done(task)
        elif choice == '5':
            delete(task)
        elif choice == '6':
            break
        else:
            print("Please try again, Invalid choice. ")
if __name__ == "__main__":
    main()
