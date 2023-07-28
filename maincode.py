# main.py
import Student
import os
from Student import Student
from Files import save_data, load_data
from exceptions import InvalidOptionError

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    roll_number = input("Enter student roll number: ")

    student = Student(name, age, roll_number)
    students_data.append(student)
    save_data("students.dat", students_data)
    print("Student added successfully!")

def view_students():
    for student in students_data:
        print(student)

def search_student():
    name = input("Enter student name to search: ")
    found_students = [student for student in students_data if student.name == name]
    if found_students:
        for student in found_students:
            print(student)
    else:
        print("Student not found!")

def update_student():
    roll_number = input("Enter student roll number to update: ")
    for i, student in enumerate(students_data):
        if student.roll_number == roll_number:
            name = input("Enter updated student name: ")
            age = int(input("Enter updated student age: "))
            students_data[i] = Student(name, age, roll_number)
            save_data("students.dat", students_data)
            print("Student information updated successfully!")
            return
    print("Student not found!")

def delete_student():
    roll_number = input("Enter student roll number to delete: ")
    for i, student in enumerate(students_data):
        if student.roll_number == roll_number:
            del students_data[i]
            save_data("students.dat", students_data)
            print("Student record deleted successfully!")
            return
    print("Student not found!")

def main():
    global students_data
    try:
        students_data = load_data("students.dat")
    except Exception as e:
        students_data = []
        print(f"Error loading data: {e}")

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 1:
                add_student()
            elif choice == 2:
                view_students()
            elif choice == 3:
                search_student()
            elif choice == 4:
                update_student()
            elif choice == 5:
                delete_student()
            elif choice == 6:
                save_data("students.dat", students_data)
                print("Exiting the program...")
                break
            else:
                raise InvalidOptionError("Invalid option. Please select a valid option (1-6).")
        except ValueError:
            print("Invalid input! Please enter a number.")
        except InvalidOptionError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
