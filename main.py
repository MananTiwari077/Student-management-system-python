from student_manager import StudentManager

manager = StudentManager()
manager.load_from_file()

while True:
    print("\n--- Student Manager ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        try:
            marks = int(input("Enter marks: "))
            manager.add_student(name, marks)
            manager.save_to_file()
        except ValueError:
            print("Invalid marks")

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        name = input("Enter name: ")
        manager.search_student(name)

    elif choice == "4":
        name = input("Enter name: ")
        manager.delete_student(name)
        manager.save_to_file()

    elif choice == "5":
        name = input("Enter name: ")
        try:
            marks = int(input("Enter new marks: "))
            manager.update_student(name, marks)
            manager.save_to_file()
        except ValueError:
            print("Invalid marks")

    elif choice == "6":
        break

    else:
        print("Invalid choice")