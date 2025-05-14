from db import create_table
import crud

def menu():
    while True:
        print("\n=== Student Record Manager ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            
            while True:
                email = input("Enter email: ").strip()
                if email:
                    break
                else:
                    print("Email is required. Please enter a valid email.")

            crud.add_student(name, age, email)
        elif choice == '2':
            crud.view_students()
        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            
            while True:
                email = input("Enter new email: ").strip()
                if email:
                    break
                else:
                    print("Email is required. Please enter a valid email.")
            crud.update_student(student_id, name, age, email)
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            crud.delete_student(student_id)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    create_table()
    menu()
