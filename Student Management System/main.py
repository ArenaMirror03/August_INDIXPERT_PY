import json
import os
from student_registration import register_students
from display import display_students
from search_moblie_no import search_by_mobile
from search_qualification import search_by_qualification
from exit import exit_program

file_path = os.getcwd() + "\\data.json"

if os.path.exists(file_path): 
    with open(file_path, "r") as file:
        students = json.load(file)
else:
    students = []

while True:
    print("==========================================================")
    print(" Menu ")
    print("1. Enter student data")
    print("2. Display all student records")
    print("3. Search data by mobile number")
    print("4. Search data by qualification")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        register_students(students, file_path)

    elif choice == "2":
        display_students(students)

    elif choice == "3":
        search_by_mobile(students)

    elif choice == "4":
        search_by_qualification(students)

    elif choice == "5":
        exit_program()
        break

    else:
        print("\nInvalid choice. Please enter 1, 2, 3, 4, or 5.")