import json
import os

students = []
qualification = []
counter = 0

while True:
    print("==========================================================")
    print(" Menu:")
    print("1. Enter student data")
    print("2. Display all student records")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        num_students = int(input("Enter the number of students: "))
        for i in range(num_students):
            print("\nEnter details for student:")
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")

            qualifications = []  

            while True:
                data = int(input("Do you want to add qualification(1: Yes || 0: NO):"))
                if data == 1:
                    education = {}
                    education["qualification name"] = input("Enter your qualification: ")
                    education["Passing Year"] = input("Enter your passing year: ")
                    qualifications.append(education)
                else:
                    break

            student_data = {
                'Student ID': student_id,
                'Name': name,
                'Age': age,
                'Grade': grade,
                'Qualifications': qualifications  
            }

            students.append(student_data)  

        counter = 1  

    elif choice == "2":
        if counter == 0:
            print("The list is empty.")
        else:
            path = os.getcwd() + "\\Data.json"
            with open(path, "w") as f:
                
                f.write(json.dumps(students, indent=4))
            print("The json file is created.")

    elif choice == "3":
        print("\nExiting program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.")
