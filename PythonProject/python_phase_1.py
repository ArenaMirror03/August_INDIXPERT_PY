import json
import os

file_path = os.getcwd() + "\\jsondata.json"

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
        print("\nEnter details for student:")
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        phone_number = input("Enter your mobile number: ")  

        qualifications = []
        while True:
            user_input = int(input("Do you want to add qualification (1: Yes || 0: No): "))
            if user_input == 1:
                education = {
                    "Qualification name": input("Enter your qualification: "),
                    "Passing year": int(input("Enter your passing year: "))
                }
                qualifications.append(education)
            else:
                break

        students.append({
            'Student ID': student_id,
            'Name': name,
            'Age': age,
            'Grade': grade,
            'Phone Number': phone_number,
            'Qualification': qualifications
        })

        with open(file_path, "w") as file:
            json.dump(students, file, indent=4)
        print("Student data saved successfully!")


    elif choice == "2":
        if not students:
            print("No records available.")
        else:
            print("\nStudent Records:")
            for student in students:
                print(json.dumps(student, indent=4))


    elif choice == "3":
        if not students:
            print("No data is available.")
        else:
            search_number = input("Enter the mobile number you want to search: ")
            found = False
            for student in students:
                if student["Phone Number"] == search_number:
                    print("Student found:", json.dumps(student, indent=4))
                    found = True
                    break
            if not found:
                print("No student found with this number.")


    elif choice == "4":
        if not students:
            print("No data is available.")
        else:
            search_qualification = input("Enter the qualification you want to search: ")
            found = False
            for student in students:
                for qualify in student["Qualification"]:
                    if qualify["Qualification name"].lower() == search_qualification.lower():
                        print("Student found:", json.dumps(student, indent=4))
                        found = True
                        break
            if not found:
                print("No student found with this qualification.")


    elif choice == "5":
        print("\nExiting program. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter 1, 2, 3, 4, or 5.")