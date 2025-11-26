def tasks():
    tasks= [] #empty list
    print("========WELCOME TO TASK MANAGEMENT APP========")
    
    total_tasks=int(input("Enter how many tasks you want to add="))
  
    for i in range(1,total_tasks+1):
      tasks_name= input(f"Enter tasks {i}=")
      tasks.append(tasks_name)
    
    print(f"today's tasks are\n {tasks}")
    
    while  True:
     try:   
         operation= int(input("Enter 1-ADD\n2-UPDATE\n3-DELETE\n4-VIEW\n5-EXIT/STOP/"))
    
         if operation==1:
             add= input("ENTER TASK YOU WANT TO ADD=")
             tasks.append(add)
             print(f"Task {add} has been added successfully")
    
         elif operation==2:
             updated_val=input("ENTER THE TASK YOU WANT TO UPDATE=")
             if updated_val in tasks:
                 up= input("ENTER NEW TASK=")
                 ind=tasks.index(updated_val)
                 tasks[ind]=up
                 print(f"updated tasks{up}")
    
         elif operation==3:
             del_value=input("ENTER THE TASK TO BE DELETED=")
             if del_value in tasks:
                 ind=tasks.index(del_value)
                 del tasks[ind]
                 print(f"TASK {del_value} DELETED")
    
         elif operation==4:
             print(f"THE TOTAL NUMBER OF TASKS IS {tasks}") 
     
         elif operation==5:
             print("CLOSING THE PROGRAM")
             break
    
         else:
             print("INVALID INPUT")
     except ValueError:
         print("invalid input. please enter a valid input.")
         
tasks()    
                   
                
         
        
         
         
         
        
    