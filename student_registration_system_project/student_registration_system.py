
# -------------- student registration system project -------------------------------

# this is a function for adding student to the student list
def student_regist(first_name,last_name):
    student_fullName = f"{first_name} {last_name}"
    student_list.append(student_fullName)

# this is a function for deleting student from the student list
def student_delete(first_name,last_name):
    student_fullName = f"{first_name} {last_name}"
    student_list.remove(student_fullName)

# The list to which we add and delete elements using the two functions above
student_list =[]
print("\n")
print("----Welcome to the School Management System----\n")

while True:
    # Our menu consists of 4 separate sections     
    home = input("Press 'S' to See Student List, 'A' to Add Student Record, 'D' to Delete Student Record, 'C' to Close The Application \n").lower()
    if home == "s":                                             
        print("\n")
        print("Student Full Name     |     Student No")
        print("----------------------------------------")
    # A loop that prints the names of students in the student list and creates a student number based on the list index number  
        for i in range(len(student_list)):             
            print(f"{student_list[i]:<32} {i}")
        print("\n")

# If the user chooses to add a student from the menu, the adding student function works (function is above).
# Inside this condition, there is a loop that runs as long as the user wants to add students.
        
    if home == "a":      
        while True:      
            first_name = input("Student's first name : ").capitalize()
            last_name = input("Student's last name : ").capitalize()
            student_regist(first_name,last_name)
            print("-------------------------------------------------------------")
            print(f"** Student named {first_name} {last_name} has been successfully registered.**")
            print("-------------------------------------------------------------")
            print("\n")
            new_record = input("a new student record? (Yes/No)").lower()
            print("\n")
            if new_record == "no":
                break

   # If the user chooses to delete a student from the menu, the deleting student function works (function is above).
   # Inside this condition, there is a loop that runs as long as the user wants to add students.
            
    if home == "d":      
        while True:   
            first_name = input("Student's first name : ").capitalize()
            last_name = input("Student's last name : ").capitalize()
            student_delete(first_name,last_name)
            print("-------------------------------------------------------------")
            print(f"** Student named {first_name} {last_name} has been successfully deleted.**")
            print("-------------------------------------------------------------")
            print("\n")
            new_record = input("a new student deregistered? (Yes/No)").lower()
            print("\n")
            if new_record == "no":
                break
    
    # If the user chooses to close the application from the menu, the loop will be broken and the application will terminate.
            
    if home == "c":
        print("\n")
        print("system is shutting down...")
        break


 
    
    

