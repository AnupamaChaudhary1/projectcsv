from db import get_connection

def add_student(name, age, email):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)", (name, age, email))
        conn.commit()
        print("Student added successfully.")

def view_students():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}")
        else:
            print("No students found.")

def update_student(student_id, name, age, email):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET name = ?, age = ?, email = ? WHERE id = ?", (name, age, email, student_id))
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
