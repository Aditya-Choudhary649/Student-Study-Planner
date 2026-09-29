import json
# Student Study Planner
# A simple Python project to manage and track study tasks
try:
    with open("tasks.json","r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []
print("===================================")
print("=======Student Study Planner=======")
print("===================================")
input("\nPress Enter to Start....")
while True:
    print("\n1. Add task ")
    print("2. View Task ")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Study Statistics")
    print("7. Edit Task")
    print("8. Exit")
    n=input("\nEnter Your Choice : ")
    #Add task
    if(n=='1'):
        print("Add Task Selected")
        subject=input("Enter Name of the Subject : ")
        task=input("Enter Task : ")
        deadline=input("Enter Deadline : ")
        new_task={"subject":subject,
                  "task":task,
                  "deadline":deadline,
                  "completed":False}
        tasks.append(new_task)
        with open("tasks.json","w") as file:
            json.dump(tasks,file)
        print("\nTask Added Successfully\n")
        input("Press Enter to Continue")
    #view task
    elif(n=='2'):
        print("View Task Selected")
        if(len(tasks)==0):
            print("No task Available")
            input("\n\nPress Enter to Continue")
        else:
            print("\n=======YOUR TASKS=======")
            for number,task in enumerate(tasks,start=1):
                print(f"\nTask{number}")
                print(f"Subject : {task['subject']}")
                print(f"Task : {task['task']}")
                print(f"Deadline : {task['deadline']}")
                if(task['completed']):
                    print("Task is Completed")
                else:
                    print("Task is Pending")
            input("\n\nPress Enter to Continue")
    #complete task
    elif n == '3':
        if len(tasks) == 0:
            print("No Task Available")
            input("\n\nPress Enter to Continue")

        else:
            print("\n======= YOUR TASKS =======")

            for number, task in enumerate(tasks, start=1):

                if task['completed']:
                    status = "Completed"
                else:
                    status = "Pending"

                print(f"{number}. {task['task']} - {status}")

            try:
                task_number = int(input("Enter the task number to mark as complete: "))

                if task_number >= 1 and task_number <= len(tasks):
                    tasks[task_number - 1]["completed"] = True

                    with open("tasks.json", "w") as file:
                        json.dump(tasks, file)

                    print("Task marked as completed!")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a number.")

        input("\n\nPress Enter to Continue")
    #delete task
    elif(n=='4'):
        if len(tasks) == 0:
            print("No Tasks Available")
            input("Press Enter to Continue")

        else:
            print("\n======= YOUR TASKS =======")

            for number,task in enumerate(tasks,start=1):
                print(f"{number}. {task['task']}")

            try:
                task_number=int(input("Enter task number to delete: "))

                if task_number>=1 and task_number<=len(tasks):
                    confirm=input("Are you sure you want to delete this task? (yes/no): ")

                    if confirm.lower()=="yes":
                        deleted_task=tasks.pop(task_number-1)

                        with open("tasks.json","w") as file:
                            json.dump(tasks,file)

                        print(f"Deleted: {deleted_task['task']}")

                    else:
                        print("Task was not deleted.")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a number.")

        input("\n\nPress Enter to Continue")
    #search task
    elif(n=='5'):
        if len(tasks)==0:
            print("No Tasks Available")
            input("Press Enter to Continue")

        else:
            search=input("Enter Subject or Task to Search : ")

            found=False

            for number,task in enumerate(tasks,start=1):

                if(search.lower() in task["subject"].lower() or
                   search.lower() in task["task"].lower()):

                    print("\nTask",number)
                    print("Subject :",task["subject"])
                    print("Task :",task["task"])
                    print("Deadline :",task["deadline"])

                    if(task["completed"]):
                        print("Status : Completed")
                    else:
                        print("Status : Pending")

                    found=True

            if(found==False):
                print("No Matching Task Found")

            input("\n\nPress Enter to Continue")
    #study statistics
    elif(n=='6'):
        print("\n======= STUDY STATISTICS =======")

        total_tasks=len(tasks)

        completed_tasks=0

        for task in tasks:
            if task["completed"]:
                completed_tasks=completed_tasks+1

        pending_tasks=total_tasks-completed_tasks

        if total_tasks>0:
            completion_percentage=(completed_tasks/total_tasks)*100
            completion_percentage=round(completion_percentage)
        else:
            completion_percentage=0

        print("Total Tasks :",total_tasks)
        print("Completed Tasks :",completed_tasks)
        print("Pending Tasks :",pending_tasks)
        print("Completion :",completion_percentage,"%")

        input("\n\nPress Enter to Continue")
    #edit task
    elif(n=='7'):
        if len(tasks)==0:
            print("No Tasks Available")
            input("Press Enter to Continue")

        else:
            print("\n======= YOUR TASKS =======")

            for number,task in enumerate(tasks,start=1):
                print(f"{number}. {task['task']}")

            try:
                task_number=int(input("Enter task number to edit: "))

                if task_number>=1 and task_number<=len(tasks):

                    print("\nEnter New Details")

                    subject=input("Enter Name of the Subject : ")
                    task=input("Enter Task : ")
                    deadline=input("Enter Deadline : ")

                    tasks[task_number-1]["subject"]=subject
                    tasks[task_number-1]["task"]=task
                    tasks[task_number-1]["deadline"]=deadline

                    with open("tasks.json","w") as file:
                        json.dump(tasks,file)

                    print("\nTask Updated Successfully")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a number.")

        input("\n\nPress Enter to Continue")
    #exit loop
    elif(n=='8'):
        print("\n\nThank You")
        break
    else:
        print("Invalid Choice. Try Again")
        input("Press Enter to Continue")