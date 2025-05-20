# from db import create_table
# import crud
# import re


# def is_valid_name(name):
#     return name.replace(" ", "").isalpha()

# def is_valid_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
#     return re.match(pattern, email)


# def menu():
#     while True:
#         print("\n=== Student Record Manager ===")
#         print("1. Add Student")
#         print("2. View Students")
#         print("3. Update Student")
#         print("4. Delete Student")
#         print("5. Exit")
        
#         choice = input("Choose an option (1-5): ")

#         if choice == '1':
#             name = input("Enter name: ")
#             if not is_valid_name(name):
#                 print("❌ Name must contain alphabets only.")
#                 continue
#             age = int(input("Enter age: "))
#             address=input("Enter the address: ")
#             while True:
#                phone_input = input("Enter the phone number (10 digits): ").strip()
#                if phone_input.isdigit() and len(phone_input) == 10:
#                   phone = phone_input
#                   break
#             else:
#                  print("❌ Phone number must be exactly 10 digits. Please try again.")

            
#             while True:
#                 email = input("Enter email: ").strip()
#                 if email:
#                     break
#                 else:
#                     print("Email is required. Please enter a valid email.")
                
#             while True:
#                 email = input("Enter email: ").strip()
#                 if is_valid_email(email):
#                     break
#                 else:
#                     print("❌ Invalid email format. Please enter a valid email (e.g., user@example.com).")


#             crud.add_student(name, age, address, phone, email)
#         elif choice == '2':
#             crud.view_students()
#         elif choice == '3':
#             student_id = int(input("Enter student ID to update: "))
#             name = input("Enter new name: ")
#             age = int(input("Enter new age: "))
#             address=input("Enter the address: ")
#             while True:
#                phone_input = input("Enter the phone number (10 digits): ").strip()
#                if phone_input.isdigit() and len(phone_input) == 10:
#                   phone = phone_input
#                   break
#             else:
#                  print("❌ Phone number must be exactly 10 digits. Please try again.")
#             while True:
#                 email = input("Enter new email: ").strip()
#                 if email:
#                     break
#                 else:
#                     print("Email is required. Please enter a valid email.")
#             crud.add_student(name, age, address, phone, email)  

#         elif choice == '4':
#             student_id = int(input("Enter student ID to delete: "))
#             crud.delete_student(student_id)
#         elif choice == '5':
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid option. Try again.")

# if __name__ == "__main__":
#     create_table()
#     crud.update_table() 
#     menu()



from db import create_table
import crud
import re

def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email)

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
            if not is_valid_name(name):
                print("❌ Name must contain alphabets only.")
                continue

            try:
                age = int(input("Enter age: "))
            except ValueError:
                print("❌ Age must be a number.")
                continue

            address = input("Enter the address: ")

            while True:
                phone_input = input("Enter the phone number (10 digits): ").strip()
                if phone_input.isdigit() and len(phone_input) == 10:
                    phone = phone_input
                    break
                else:
                    print("❌ Phone number must be exactly 10 digits. Please try again.")

            while True:
                email_input = input("Enter email: ").strip()
                if is_valid_email(email_input):
                    email = email_input
                    break
                else:
                    print("❌ Invalid email format. Please enter a valid email (e.g., user@example.com).")

            crud.add_student(name, age, address, phone, email)

        elif choice == '2':
            crud.view_students()

        elif choice == '3':
            try:
                student_id = int(input("Enter student ID to update: "))
            except ValueError:
                print("❌ Student ID must be a number.")
                continue

            name = input("Enter new name: ")
            if not is_valid_name(name):
                print("❌ Name must contain alphabets only.")
                continue

            try:
                age = int(input("Enter new age: "))
            except ValueError:
                print("❌ Age must be a number.")
                continue

            address = input("Enter the address: ")

            while True:
                phone_input = input("Enter the phone number (10 digits): ").strip()
                if phone_input.isdigit() and len(phone_input) == 10:
                    phone = phone_input
                    break
                else:
                    print("❌ Phone number must be exactly 10 digits. Please try again.")

            while True:
                email_input = input("Enter new email: ").strip()
                if is_valid_email(email_input):
                    email = email_input
                    break
                else:
                    print("❌ Invalid email format. Please enter a valid email (e.g., user@example.com).")

            crud.update_student(student_id, name, age, address, phone, email)

        elif choice == '4':
            try:
                student_id = int(input("Enter student ID to delete: "))
                crud.delete_student(student_id)
            except ValueError:
                print("❌ Student ID must be a number.")

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    create_table()
    crud.update_table()
    menu()
