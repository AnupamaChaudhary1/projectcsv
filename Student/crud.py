# from db import get_connection

# def add_student(name, age, address, phone, email):
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO students (name, age, address, phone, email) VALUES (?, ?, ?,?,?)", (name, age, address, phone, email))
#         conn.commit()
#         print("Student added successfully.")

# def view_students():
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM students")
#         rows = cursor.fetchall()
#         if rows:
#             for row in rows:
#                 print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]},  Address: {row[3]}, Phone: {row[4]}  Email: {row[5]}")
#         else:
#             print("No students found.")

# def update_student(student_id, name, age, address, phone, email):
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("UPDATE students SET name = ?, age = ?, address=?, phone=?, email = ? WHERE id = ?", (name, age, address, phone, email,  student_id))
#         if cursor.rowcount == 0:
#             print("Student ID not found.")
#         else:
#             conn.commit()
#             print("Student updated successfully.")

# def delete_student(student_id):
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
#         if cursor.rowcount == 0:
#             print("Student ID not found.")
#         else:
#             conn.commit()
#             print("Student deleted successfully.")

# def update_table():
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("PRAGMA table_info(students)")
#         columns = [col[1] for col in cursor.fetchall()]

#         if "address" not in columns:
#             cursor.execute("ALTER TABLE students ADD COLUMN address TEXT")
#         if "phone" not in columns:
#             cursor.execute("ALTER TABLE students ADD COLUMN phone TEXT")

#         conn.commit()


from db import get_connection

def add_student(name, age, address, phone, email):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, address, phone, email) VALUES (?, ?, ?, ?, ?)",
            (name, age, address, phone, email)
        )
        conn.commit()
        print("Student added successfully.")

def view_students():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Address: {row[4]}, Phone: {row[5]} Email: {row[3]}")
        else:
            print("No students found.")

def update_student(student_id, name, age, address, phone, email):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE students SET name = ?, age = ?, address = ?, phone = ?, email = ? WHERE id = ?",
            (name, age, address, phone, email, student_id)
        )
        if cursor.rowcount == 0:
            print("Student ID not found.")
        else:
            conn.commit()
            print("Student updated successfully.")

def delete_student(student_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        if cursor.rowcount == 0:
            print("Student ID not found.")
        else:
            conn.commit()
            print("Student deleted successfully.")

def update_table():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(students)")
        columns = [col[1] for col in cursor.fetchall()]

        if "address" not in columns:
            cursor.execute("ALTER TABLE students ADD COLUMN address TEXT")
        if "phone" not in columns:
            cursor.execute("ALTER TABLE students ADD COLUMN phone TEXT")

        conn.commit()
