from src.tasks import TaskManager
from utils.clear import Clear
from time import sleep

manager = TaskManager()

while True:
    Clear()
    print("--- Task Manager ---")
    print("[1] New task\n[2] List all tasks\n[0] Exit\n")

    menu_choice = int(input("Select an option: "))

    if menu_choice == 0:
        print("\033[31mEnding program...\033[m")
        sleep(2)
        Clear()
        manager.close()
        break

    if menu_choice == 1:
        Clear()
        print("--- Task Creation Page ---\n")
        new_task = input("New task (0 to cancel): ")

        if new_task in '0':
            print("\033[31mGoing back...\033[m")
            sleep(2)
            break

        manager.reset()
        manager.add_task(new_task, 'active')

    elif menu_choice == 2:
        while True:
            Clear()
            tasks = manager.list_tasks()

            for ids, task, status, entry in tasks:
                print(f"[{ids}] {task} / {status} / {entry}")

            print("--------\n[1] Change task status\n[2] Delete tasks\n[3] Go back")
            list_choice = int(input("Select an option: "))

            if list_choice == 1:
                while True:
                    task_id = int(input("Enter task ID to change status: "))
                    new_status = input("New status (Active/Inactive/Completed): ")

                    print("--------")
                    print(manager.change_task_status(task_id, new_status))
                    sleep(2)
                    break
        
            elif list_choice == 2:
                while True:
                    task_id = int(input("Enter task ID to delete: "))

                    if manager.task_exists(task_id):
                        manager.delete_task(task_id)
                        print(f"Task with ID {task_id} successfully deleted.")
                        sleep(2)
                        break
                    else:
                        print("Task ID not found")
                        sleep(2)
                        continue

            elif list_choice == 3:
                print("\033[31mGoing back...\033[m")
                sleep(2)
                break