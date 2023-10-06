# Importing the datetime module to use to compare dates later on in the code i.e. to tell if a task managed is overdue.
from datetime import datetime 

# Firstly, a few functions need to be defined for use in the program. After that we will declare admin menu and it's options then user menu
# I have chosen not to make use of "global" as it stopped the program from running
# Function to create dictionary of username/password combinations
def username_check() :

    # Declare local variables    
    users = {}

    # Access "user.txt" file in read mode    
    with open("user.txt", "r") as f :

        # Run through "user.txt" file to check for matching combination        
        for line in f :
            user_check = line.strip("\n")
            
            # Prevent range out of bound errors as caused by empty lines            
            if user_check != "" :
                user_check = user_check.split(", ")
                users.update({user_check[0]: user_check[1]})

    return users

# Function to create a list of tasks
def task_check() :

    # Declare local variables    
    tasks = []
    count = 1

    # Access "tasks.txt" file in read mode    
    with open("tasks.txt", "r") as f :

        # Run through "tasks.txt" file to check for matching combination        
        for line in f :
            task_check = line.strip("\n")
            
            #Prevent range out of bound errors as caused by empty lines            
            if task_check != "" :
                task_check = [task_check.split(", ") + [count]]
                tasks.extend(task_check)
                count += 1

    return tasks        

# Function select a task for later in the vm option
def select_task() :

    #Get list of tasks
    tasks = task_check()

    # Declare local variables
    task_selection = True

    # While loop to get desired task number input
    while(task_selection) :

        task_number = input("Please enter your task reference or '-1' to return to menu:\n")
        
        try :
            task_number = int(task_number)

        except :
            print("Invalid input\n")

        if task_number == -1 :
            print()
            task_selection = False
            return

        else :
            for i in range(0, len(tasks)) :
        
                # If user and assigned_user are the same plus task_number matches task reference, alow user to edit task or mark complete
                if task_number == tasks[i][6] and tasks[i][5].lower() == "yes" :
                    print(f"task reference {task_number} is already complete, no further editing is permitted\n")
                    
                elif username == tasks[i][0] and task_number == tasks[i][6] :
                    modify_or_complete = input("Please enter 'mk' to mark task as complete or 'ed' to edit task?\n")
                    print()

                    if modify_or_complete.lower() != 'mk' and modify_or_complete.lower() != 'ed' :
                        print("Invalid input.\n")

                    elif modify_or_complete.lower() == 'mk' :
                        mark_task(task_number)
                        return

                    else :
                        edit_task(task_number)
                        return

# Function to mark task as complete for later use in the vm choice                        
def mark_task(task_number) :

    # Get list of tasks
    tasks = task_check() # Calling on task check function

    # Declare local variables    
    string_task = ""

    # Check for matching task number and amend completed statement to "yes"    
    for i in range(0, len(tasks)) :
        if task_number == tasks[i][6] :
                   tasks[i][5] = "yes"

        # Remove number added in by task_check() function                   
        tasks[i].pop()

        # Store each task in variable to be written to "tasks.txt" file        
        string_task += ", ".join(tasks[i]) + "\n"

    # Open "tasks.txt" in write mode and write the variable "string_task" to file
    with open("tasks.txt", "w") as f :
        f.write(string_task)
    

# Function to edit assigned user and/or due date for later use in the vm option
def edit_task(task_number) :
    
    #Get list of tasks and users
    tasks = task_check()
    user_list = username_check()

    # Declare local variables    
    string_task = ""
    editing = True
    
    # Check if user would like to edit assigned person or due date
    while(editing) :
        user_or_date = input("Please enter 'user' to edit task assignment, 'date' to edit due date or 'both' to edit both:\n")

        if user_or_date.lower() == "user" :

            # Have user enter newly assigned user, checking that username exists
            new_user = input("Please enter the username to which this task should be assigned:\n")

            if new_user in user_list :
                for i in range(0, len(tasks)) :
                    if task_number == tasks[i][6] :
                        tasks[i][0] = new_user

                    # Remove number added in as part of task_check() function
                    tasks[i].pop()
                    string_task += ", ".join(tasks[i]) + "\n"
                    
                editing = False
                
            else :
                print("Username does not exist\n")
            
        # Have user enter in new due date                
        elif user_or_date.lower() == "date" :
            new_date = input("Please enter when the task is due in dd-mmm-yyyy format:\n")
            for i in range(0, len(tasks)) :
                if task_number == tasks[i][6] :
                    tasks[i][4] = new_date
                tasks[i].pop()
                string_task += ", ".join(tasks[i]) + "\n"
                editing = False

        # Have user enter new assigned user, checking that username exists, and enter new due date                
        elif user_or_date.lower() == "both" :
            new_user = input("Please enter the username to which this task should be assigned:\n")
            if new_user in user_list :
                new_date = input("Please enter when the task is due in dd-mmm-yyyy format:\n")

                for i in range(0, len(tasks)) :
                    if task_number == tasks[i][6] :
                        tasks[i][0] = new_user
                        tasks[i][4] = new_date
        
                    tasks[i].pop()
                    string_task += ", ".join(tasks[i]) + "\n"
                    editing = False
            else :
                print("Username does not exist\n")

    # Open "tasks.txt" file in write mode and write the variable "string_task" to it
    with open("tasks.txt", "w") as f :
        f.write(string_task)

# Define a function to select a task later in the vm option
def select_task() :

    #Get list of tasks
    tasks = task_check()

    #Declare local variables
    task_selection = True

    # While loop to get desired task number input
    while(task_selection) :
        task_number = input("Please enter your task reference or '-1' to return to menu:\n")
        
        try :
            task_number = int(task_number)
        except :
            print("Invalid input\n")

        if task_number == -1 :
            print()
            task_selection = False
            return

        else :
            for i in range(0, len(tasks)) :
        
                # If user and assigned_user are the same plus task_number matches task reference, alow user to edit task or mark complete
                if task_number == tasks[i][6] and tasks[i][5].lower() == "yes" :
                    print(f"task reference {task_number} is already complete, no further editing is permitted\n")
                    
                elif username == tasks[i][0] and task_number == tasks[i][6] :
                    modify_or_complete = input("Please enter 'mk' to mark task as complete or 'ed' to edit task?\n")
                    print()

                    if modify_or_complete.lower() != "mk" and modify_or_complete.lower() != 'ed' :
                        print("Invalid input.\n")

                    elif modify_or_complete.lower() == "mk":
                        mark_task(task_number)
                        return

                    else :
                        edit_task(task_number)
                        return

# Function to mark task as complete                        
def mark_task(task_number) :

    #Get list of tasks
    tasks = task_check() # Calling on task check function

    # Declare local variables    
    string_task = ""

    # Check for matching task number and amend completed statement to "yes"    
    for i in range(0, len(tasks)) :
        if task_number == tasks[i][6] :
                   tasks[i][5] = "yes"

        # Remove number added in by task_check() function                   
        tasks[i].pop()

        # Store each task in variable to be written to "tasks.txt" file        
        string_task += ", ".join(tasks[i]) + "\n"

    # Open "tasks.txt" in write mode and write the variable "string_task" to file
    with open("tasks.txt", "w") as f :
        f.write(string_task)
    

# Function to edit assigned user and/or due date for later use in vm option    
def edit_task(task_number) :
    
    # Get list of tasks and users. Calling on task check and username check functions
    tasks = task_check()
    user_list = username_check()

    # Declare local variables    
    string_task = ""
    editing = True
    
    # Check if user would like to edit assigned person or due date
    while(editing) :
        user_or_date = input("Please enter 'user' to edit task assignment, 'date' to edit due date or 'both' to edit both:\n")

        if user_or_date.lower() == "user" :

            # Have user enter newly assigned user, checking that username exists
            new_user = input("Please enter the username to which this task should be assigned:\n")

            if new_user in user_list :
                for i in range(0, len(tasks)) :
                    if task_number == tasks[i][6] :
                        tasks[i][0] = new_user

                    # Remove number added in as part of task_check() function
                    tasks[i].pop()
                    string_task += ", ".join(tasks[i]) + "\n"
                    
                editing = False
                
            else :
                print("Username does not exist\n")
            
        # Have user enter in new due date                
        elif user_or_date.lower() == "date" :
            new_date = input("Please enter when the task is due in dd-mm-yyyy format:\n")
            for i in range(0, len(tasks)) :
                if task_number == tasks[i][6] :
                    tasks[i][4] = new_date
                tasks[i].pop()

                string_task += ", ".join(tasks[i]) + "\n"

                editing = False

        # Have user enter new assigned user, checking that username exists, and enter new due date                
        elif user_or_date.lower() == "both" :
            new_user = input("Please enter the username to which this task should be assigned:\n")
            if new_user in user_list :
                new_date = input("Please enter when the task is due in dd-mmm-yyyy format:\n")

                for i in range(0, len(tasks)) :
                    if task_number == tasks[i][6] :
                        tasks[i][0] = new_user
                        tasks[i][4] = new_date

        
                    tasks[i].pop()
                    string_task += ", ".join(tasks[i]) + "\n"
                    editing = False
            else :
                print("Username does not exist\n")

    # Open "tasks.txt" file in write mode and write the variable "string_task" to it
    with open("tasks.txt", "w") as f :
        f.write(string_task)

# Function for admin menu only with its own options
def admin_menu():
    choice = input("""\nPlease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
""").lower()
    
    # If they want to register the user, 
    if choice == "r":
        def register_user():
            username = input("\nPlease enter a username: ").lower()
            password = input("Please enter a password: ").lower()
            confirm_password = input("Please confirm your password: ").lower()
            with open("user.txt", "a") as file1:
                if password == confirm_password:
                    file1.write(f"\n{username}, {password}\n")
                    print("\nUser successfully registered.")
                    
                    
        # Calling back the register user as well as admin_menu functions
        register_user()
        admin_menu()

    # Function for if the want to add a task and the choice is "a"    
    elif choice == "a":
        tasks_dict = {}
        def add_task():
            count = 0
            with open("tasks.txt", "a") as file2:
                user_assignment = input("\nPlease enter the user assigned to this task: ").lower()
                title = input("\nPlease enter a task title: ")
                description = input("\nPlease enter a description: ")                
                date_today = input("\nPlease enter the current date as dd-mm-yyyy: ")
                current_date = datetime.strftime(datetime.strptime(date_today, "%d-%m-%Y"), '%d %b %Y')
                user_due_date_input = input("\nPlease enter the task due date as dd-mm-yyyy: ")
                formatted_due_date = datetime.strftime(datetime.strptime(user_due_date_input, "%d-%m-%Y"), '%d %b %Y')
                status = ("No").lower()
                file2.write(f'\n{user_assignment}, {title}, {description}, {current_date}, {formatted_due_date}, {status}')
                print("\nTask added.")
                 
            # Casting all the user input info into a list, to add to the tasks_dict.
                task_list = [user_assignment, title, description, current_date, formatted_due_date, status]
                tasks_dict[f"Task {count} details:"] = task_list
                count = count + 1
                return tasks_dict
            
        
        # Calling back the add_task and admin_menu functions    
        add_task()
        admin_menu()

    # If they choose to view all... Function for view all declared        
    elif choice == "va":
        def view_all_option():
            tasks = task_check() # Caliing on the task Check function
    
            # Loop through each tasks to print them    
            for i in range(0, len(tasks)) :
        
                # Print task in a user friendly manner        
                print("-"*50)
                print(f"Task:\t\t\t{tasks[i][1]}")
                print(f"Assigned to:\t\t{tasks[i][0]}")
                print(f"Date assigned:\t\t{tasks[i][3]}")
                print(f"Due date:\t\t{tasks[i][4]}")
                print(f"Task complete?\t\t{tasks[i][5]}")
                print(f"Task description:\n{tasks[i][2]}")
    
            print("-"*50)
            print()
            
            
        # Calling the function for view all and admin menu
        view_all_option()
        admin_menu()

    # Function for if they view only their tasks by choosing vm    
    elif choice == "vm":
        def view_mine():       
            tasks = task_check() # Caliing on the task Check function
    
            # Loop through each tasks to print them    
            for i in range(0, len(tasks)) :
        
                # If user and assigned_user are the same, print task in a user friendly manner        
                if username == tasks[i][0] :
                    print("-"*50)
                    print(f"Task reference:\t\t{tasks[i][6]}")
                    print(f"Task:\t\t\t{tasks[i][1]}")
                    print(f"Assigned to:\t\t{tasks[i][0]}")
                    print(f"Date assigned:\t\t{tasks[i][3]}")
                    print(f"Due date:\t\t{tasks[i][4]}")
                    print(f"Task complete?\t\t{tasks[i][5]}")
                    print(f"Task description:\n{tasks[i][2]}")
    
        print("-"*50)
        print()


        # Calling back the view mine, select task and admin menu        
        view_mine()
        select_task()           
        admin_menu()

    # If they choose to generate a report, Function for gr choice    
    elif choice == "gr":
        def generate_reports():

            # Get task list and user list by calling on task check and usename check functions 
            task = task_check()
            users = username_check()

            # Convert dictionary "users" to a list of key values    
            users = [*users]

            # Declare local variables    
            total = len(task)
            total_users = len(users)
            complete = 0
            incomplete = 0
            overdue = 0
            percent_incomplete = 0
            percent_overdue = 0

            # Find and keep count of all tasks, incomplete tasks and overdue tasks
            for i in range(0, total) :
                if task[i][5] == "yes" :
                    complete += 1
                elif task[i][5] == "no" and datetime.strptime(task[i][4], '%d %b %Y') < datetime.now():
                    incomplete += 1
                    overdue += 1
                    percent_incomplete = (incomplete / total) * 100
                    percent_overdue = (overdue / total) * 100
        
                elif task[i][5] == "no" :
                    incomplete += 1
                    percent_incomplete = (incomplete / total) * 100
            
            #Generate "task_overview.txt" file in an easy to read manner            
            with open("task_overview.txt", "w") as f :
                f.write(f"Number of tasks\t\t- {total}\n")
                f.write(f"Number completed\t- {complete}\n")
                f.write(f"Number incomplete\t- {incomplete}\n")
                f.write(f"Number overdue\t\t- {overdue}\n")
                f.write(f"Percentage incomplete\t- {percent_incomplete:.2f}%\n")
                f.write(f"Percentage overdue\t- {percent_overdue:.2f}%\n")

            # Generate "user_overview.txt" filen an easy to read manner        
            with open("user_overview.txt", "w") as g :
                g.write(f"Total users\t- {total_users}\n")
                g.write(f"Total tasks\t- {total}\n\n")

                # Loop through users to seperate tasks by their specific assigned user        
                for i in range(0, total_users) :
            
                    #Local variables declared within for loop to prevent double counting from occurring
                    user_tasks = 0
                    completed = 0
                    not_complete = 0
                    user_overdue = 0
                    task_percent = 0
                    complete_percent = 0
                    incomplete_percent = 0
                    overdue_percent = 0

            # Loop through specific user tasks to find completion status and due dates. Count of number of tasks, completed or not and due date maintained            
                    for j in range(0, total) :
                        if users[i] == task[j][0] and task[j][5] == "yes":
                            user_tasks += 1
                            completed += 1                    
                    
                        elif users[i] == task[j][0] and task[j][5] == "no" and datetime.strptime(task[j][4], '%d %b %Y') < datetime.now():
                            user_tasks += 1
                            not_complete += 1
                            user_overdue += 1
                    
                        elif users[i] == task[j][0] and task[j][5] == "no" :
                            user_tasks += 1
                            not_complete += 1
                    
                        # Calculate user percentages, ensuring that 0 assigned tasks does not result in a divide by 0 error                    
                        task_percent = (user_tasks / total) * 100
                        if user_tasks != 0 :
                            complete_percent = (completed / user_tasks) * 100
                            incomplete_percent = (not_complete / user_tasks) * 100
                            overdue_percent = (user_overdue / user_tasks) * 100
                    
                    # Write the results to the file before progressing to the next registered user        
                    g.write("-" * 50 + "\n")
                    g.write(f"User: {users[i]}\n\n")
                    g.write(f"Number of user tasks\t\t- {user_tasks}\n")
                    g.write(f"Percentage of total tasks\t- {task_percent:.2f}%\n")
                    g.write(f"Percentage completed\t\t- {complete_percent:.2f}%\n")
                    g.write(f"Percentage incomplete\t\t- {incomplete_percent:.2f}%\n")
                    g.write(f"Percentage overdue\t\t- {overdue_percent:.2f}%\n")    
        
        
        # Calling back generate reports and admin menu
        generate_reports()
        admin_menu()

    # Function for statistics for admin only if they choose ds I have added in defensive blocks   
    elif username == "admin" and choice == "ds":
        def display_statistics():
            task_file = "task_overview.txt"
            user_file = "user_overview.txt"
            try:
                with open(task_file, "r") as task_report:
                    task_data = task_report.read()
                    print("Task Overview Report: ")
                    print(task_data)
    
                with open(user_file, "r") as user_report:
                    user_data = user_report.read()
                    print("\nUser Overview Report: ")
                    print(user_data)
            except FileNotFoundError:
                print("Reports not found. Make sure the files exist.")


        # Calling back display stats and admin menu functions        
        display_statistics()
        admin_menu()
        
    # If they want to exit the program, a simple print statement ends it
    elif choice == "e":
        print("Exiting Task Manager. Goodbye!")
        
# Function for admin menu only with its own options        
def user_menu():
    choice = input("""\nPlease select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
e - exit
""").lower()
    
    # Function for if the want to add a task and the choice is "a"     
    if choice == "a":
        tasks_dict = {}
        def add_task():
            count = 0
            with open("tasks.txt", "a") as file2:
                user_assignment = input("\nPlease enter the user assigned to this task: ").lower()
                title = input("\nPlease enter a task title: ")
                description = input("\nPlease enter a description: ")
                user_due_date_input = input("\nPlease enter the task due date as dd-mm-yyyy: ")
                formatted_due_date = datetime.strftime(datetime.strptime(user_due_date_input, "%d-%m-%Y"), '%d %b %Y')
                date_today = input("\nPlease enter the current date as dd-mm-yyyy: ")
                current_date = datetime.strftime(datetime.strptime(date_today, "%d-%m-%Y"), '%d %b %Y')
                status = ("No").lower()
                file2.write(f'\n{user_assignment}, {title}, {description}, {formatted_due_date}, {current_date}, {status}\n')
                print("\nTask added.")
                 
                # Casting all the user input info into a list, to add to the tasks_dict.
                task_list = [user_assignment, title, description, current_date, formatted_due_date, status]
                tasks_dict[f"Task {count} details:"] = task_list
                count = count + 1
                return tasks_dict
            
            
        # Calling back the add task and user menu functions
        add_task()
        user_menu()

    # If they choose to view all... Function for view all declared         
    elif choice == "va":
        def view_all_option():
            tasks = task_check() # Caliing on the task Check function
    
            # Loop through each tasks to print them    
            for i in range(0, len(tasks)) :
        
                # Print task in a user friendly manner        
                print("-"*50)
                print(f"Task:\t\t\t{tasks[i][1]}")
                print(f"Assigned to:\t\t{tasks[i][0]}")
                print(f"Date assigned:\t\t{tasks[i][3]}")
                print(f"Due date:\t\t{tasks[i][4]}")
                print(f"Task complete?\t\t{tasks[i][5]}")
                print(f"Task description:\n{tasks[i][2]}")
    
            print("-"*50)
            print()


        # Calling back the view all and user menu functions
        view_all_option()
        user_menu()

    # Function for if they view only their tasks by choosing vm    
    elif choice == "vm":
        def view_mine():       
            tasks = task_check() # Caliing on the task Check function
    
            # Loop through each tasks to print them    
            for i in range(0, len(tasks)) :
        
                # If user and assigned_user are the same, print task in a user friendly manner        
                if username == tasks[i][0] :
                    print("-"*50)
                    print(f"Task reference:\t\t{tasks[i][6]}")
                    print(f"Task:\t\t\t{tasks[i][1]}")
                    print(f"Assigned to:\t\t{tasks[i][0]}")
                    print(f"Date assigned:\t\t{tasks[i][3]}")
                    print(f"Due date:\t\t{tasks[i][4]}")
                    print(f"Task complete?\t\t{tasks[i][5]}")
                    print(f"Task description:\n{tasks[i][2]}")
    
        print("-"*50)
        print()


        # Calling on the view mine, select task and user menu        
        view_mine()
        select_task()
        user_menu()

    # If they choose to generate a report, Function for gr choice        
    elif choice == "gr":
        def generate_reports():

            # Get task list and user list by calling on task check and username check functions 
            task = task_check()
            users = username_check()

            # Convert dictionary "users" to a list of key values    
            users = [*users]

            # Declare local variables    
            total = len(task)
            total_users = len(users)
            complete = 0
            incomplete = 0
            overdue = 0
            percent_incomplete = 0
            percent_overdue = 0

            # Find and keep count of all tasks, incomplete tasks and overdue tasks
            for i in range(0, total) :
                if task[i][5] == "yes" :
                    complete += 1
                elif task[i][5] == "no" and datetime.strptime(task[i][4], '%d %b %Y') < datetime.now():
                    incomplete += 1
                    overdue += 1
                    percent_incomplete = (incomplete / total) * 100
                    percent_overdue = (overdue / total) * 100
        
                elif task[i][5] == "no" :
                    incomplete += 1
                    percent_incomplete = (incomplete / total) * 100
            
            # Generate "task_overview.txt" file in an easy to read manner            
            with open("task_overview.txt", "w") as f :
                f.write(f"Number of tasks\t\t- {total}\n")
                f.write(f"Number completed\t- {complete}\n")
                f.write(f"Number incomplete\t- {incomplete}\n")
                f.write(f"Number overdue\t\t- {overdue}\n")
                f.write(f"Percentage incomplete\t- {percent_incomplete:.2f}%\n")
                f.write(f"Percentage overdue\t- {percent_overdue:.2f}%\n")

            # Generate "user_overview.txt" file in an easy to read manner        
            with open("user_overview.txt", "w") as g :
                g.write(f"Total users\t- {total_users}\n")
                g.write(f"Total tasks\t- {total}\n\n")

                # Loop through users to seperate tasks by their specific assigned user        
                for i in range(0, total_users) :
            
                    # Local variables declared within for loop to prevent double counting from occurring        
                    user_tasks = 0
                    completed = 0
                    not_complete = 0
                    user_overdue = 0
                    task_percent = 0
                    complete_percent = 0
                    incomplete_percent = 0
                    overdue_percent = 0

                    # Loop through specific user tasks to find completion status and due dates. Count of number of tasks, completed or not and due date maintained            
                    for j in range(0, total) :
                        if users[i] == task[j][0] and task[j][5] == "yes":
                            user_tasks += 1
                            completed += 1
                                        
                        elif users[i] == task[j][0] and task[j][5] == "no" and datetime.strptime(task[j][4], '%d %b %Y') < datetime.now():
                            user_tasks += 1
                            not_complete += 1
                            user_overdue += 1
                    

                        elif users[i] == task[j][0] and task[j][5] == "no" :
                            user_tasks += 1
                            not_complete += 1
                    
                        # Calculate user percentages, ensuring that 0 assigned tasks does not result in a divide by 0 error                    
                        task_percent = (user_tasks / total) * 100
                        if user_tasks != 0 :
                            complete_percent = (completed / user_tasks) * 100
                            incomplete_percent = (not_complete / user_tasks) * 100
                            overdue_percent = (user_overdue / user_tasks) * 100
                    
                    # Write the results to the file before progressing to the next registered user        
                    g.write("-" * 50 + "\n")
                    g.write(f"User: {users[i]}\n\n")
                    g.write(f"Number of user tasks\t\t- {user_tasks}\n")
                    g.write(f"Percentage of total tasks\t- {task_percent:.2f}%\n")
                    g.write(f"Percentage completed\t\t- {complete_percent:.2f}%\n")
                    g.write(f"Percentage incomplete\t\t- {incomplete_percent:.2f}%\n")
                    g.write(f"Percentage overdue\t\t- {overdue_percent:.2f}%\n")    
        
        
        # Calling back the generate reports and user menu functions
        generate_reports()
        user_menu()
    
    # If they choose to exit the program, a simple print statement will do that
    elif choice == "e":
        print("Exiting Task Manager. Goodbye!")    
        
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
        
# Writing the program.    
# Firstly, I will build the current info from tasks.txt and user.txt into appropriate lists and dictionaries.
# This will allow me to build and work with the information in an easier way. 
# In the first version of this code, I used a string to store the user and task contents.
# Now, the user and tasks details will be stored in corresponding dictionaries for use in the program.
user_details = {}

# The user details dictionary will be built with lists from 'usernames_list' and 'passwords_list' as values.
usernames_list = []
passwords_list = []

tasks_dict = {}

# Opening the tasks.txt file to read and write information from it.
# Adding the info in the user.txt file into the set list.
with open('user.txt', 'r+') as f:

    for line in f:

        newline = line.rstrip('\n')  # Stripping newline characters from the line.
        
        split_line = newline.split(", ")  # Splitting the line into a list.
        
        usernames_list.append(split_line[0])  # Assigning items from the list into corresponding list.
        passwords_list.append(split_line[1])

        user_details["Usernames"] = usernames_list  # Lists are now stored as values assigned to keys in user_details dictionary.
        user_details["Passwords"] = passwords_list      


# Setting a count to keep track of the number of lines in the tasks.txt file.
count = 1

# Opening the tasks.txt file to read and write information to it.
with open('tasks.txt', 'r+') as f2:

    for line in f2:

        
        newline = line.rstrip('\n')  # Stripping newline characters.
        
        split_line = newline.split(", ")  # Splitting line into a list of items.

        tasks_dict[f"Task {count} details:"] = split_line # Assigning each list of items to a key in tasks_dict.

        count += 1  # Count used to change key value for each list of info.


# Writing the program for the task manager.
# Getting input from the user on their login details.
username = input("Please enter your username: \n")
password = input("Please enter your password: \n")

# Creating a while loop to run indefinitely whilst login details are incorrect.
# Appropriate error messages are displayed.
# Use of the words 'in' and 'not in' used to test whether the username and password appear in the appropriate lists.
while (username not in usernames_list) or (password not in passwords_list):

        # If username is correct and password is correct, the following message is displayed.
        if (username not in usernames_list) and (password in passwords_list):

            print("Your username is not listed.")

            username = input("Please re-enter your username: \n")  # User is prompted to re-enter details. 
            password = input("Please re-enter your password: \n")

        # If password is incorrect and username is correct, the following message is displayed.
        elif (password not in passwords_list) and (username in usernames_list):

            print("Your password is incorrect.")

            username = input("Please re-enter your username: \n")
            password = input("Please re-enter your password: \n")

        # If both the username and password are incorrect, the following message is displayed. 
        elif (username not in usernames_list) and (password not in passwords_list):

            print("Your username and password are incorrect.")

            username = input("Please re-enter your username: \n")
            password = input("Please re-enter your password: \n")

# If both username and password are correct, the successful login message is displayed.            
if (username in usernames_list) and (password in passwords_list):

    print("You are successfully logged in.")

if username == "admin":
    admin_menu()
else:
    user_menu()