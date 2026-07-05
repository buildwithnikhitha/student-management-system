import json

students = []

#-------------LOAD DATA---------------
def load_students():
    global students
    try:
        with open("students.json","r") as file:
            students = json.load(file)
    except FileNotFoundError:
            students = []

#--------------SAVE STUDENTS-------------
def save_students():
    with open("students.json","w")as file:
        json.dump(students,file,indent=4)            

#--------------ADD STUDENT---------------
def add_student():
    while True:
        name = input("Enter Student Name: ")
        if name.strip() == "":
            print("Name cannot be empty!")
        else:
            break

    roll = input("Enter Roll Number: ")

    # duplicate check
    for student in students:
        if student["roll"] == roll:
            print("Roll Number Already Exists!")
            return

    branch = input("Enter Branch: ")

    student = {
        "name": name,
        "roll": roll,
        "branch": branch
    }

    students.append(student)
    save_students()
    print("Student Added Successfully")

#-------------VIEW STUDENTS--------------
def view_students():
    if not students:
        print("No Students Found")
        return

    print("\nName\tRoll\tBranch")
    print("---------------------------")

    for s in students:
        print(f"{s['name']}\t{s['roll']}\t{s['branch']}")

#--------------SEARCH STUDENTS---------------
def search_student():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            print(f"Name: {s['name']} | Roll: {s['roll']} | Branch: {s['branch']}")
            return

    print("Student Not Found")

#--------------DELETE STUDENT--------------
def delete_student():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            confirm = input("Are you sure? (yes/no): ")

            if confirm.lower() == "yes":
                students.remove(s)
                save_students()
                print("Student Deleted")
            else:
                print("Delete Cancelled")
            return

    print("Student Not Found")

#------------UPDATE STUDENT--------------
def update_student():
    roll = input("Enter Roll Number to Update: ")

    for s in students:
        if s["roll"] == roll:
            print("Current Data:",s)

            s["name"] = input("Enter New Name: ")
            s["branch"] = input("Enter New Branch: ")
            save_students()
            print("Student Updated Successfully")
            return

    print("Student Not Found")

#----------MAIN PROGRAM-----------
load_students()

while True:
    print("\n===== Student Management System =====")
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        update_student()
    elif choice == "6":
        print("Exiting... Bye!")
        break
    else:
        print("Invalid choice")