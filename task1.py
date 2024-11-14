class Task:
    def __init__(self, description):
        self.description = description
        self.is_completed = False

    def get_description(self):
        return self.description

    def is_completed(self):
        return self.is_completed

    def set_completed(self, completed):
        self.is_completed = completed

    def __str__(self):
        return f"{self.description} - {'Completed' if self.is_completed else 'Not Completed'}"

class TodoListApp:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        description = input("Enter the task description: ")
        self.tasks.append(Task(description))
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def mark_task_completed(self):
        self.view_tasks()
        if self.tasks:
            task_number = int(input("Enter task number to mark as completed: "))
            if 0 < task_number <= len(self.tasks):
                self.tasks[task_number - 1].set_completed(True)
                print("Task marked as completed.")
            else:
                print("Invalid task number.")

    def delete_task(self):
        self.view_tasks()
        if self.tasks:
            task_number = int(input("Enter task number to delete: "))
            if 0 < task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number - 1)
                print(f"Task '{removed_task.get_description()}' deleted.")
            else:
                print("Invalid task number.")

    def run(self):
        print("Welcome to the To-Do List Application!")

        while True:
            print("\nChoose an option:")
            print("1 - Add Task")
            print("2 - View Tasks")
            print("3 - Mark Task as Completed")
            print("4 - Delete Task")
            print("5 - Exit")

            choice = int(input("Choice:"))

            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.view_tasks()
            elif choice == 3:
                self.mark_task_completed()
            elif choice == 4:
                self.delete_task()
            elif choice == 5:
                print("Exiting To-Do List Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    TodoListApp().run()

