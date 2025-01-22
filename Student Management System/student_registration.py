import json
import os

def register_students(students, file_path):
    print("\nEnter details for student:")
    student_id = None
    while True:
        student_input = input("Enter student ID: ")
        if student_input.isdigit():            
            if any(student['Student ID'] == student_id for student in students):
                print("Error: Student ID already exists. Please enter a different ID.")
            else:
                student_id = int(student_input) 
                break
        else:
            print("Error: Only numbers are allowed for student ID. Please try again.")
    
    name = None
    while True:
        name_input = input("Enter student name: ")
        if not name_input.isalpha():
            print("Error: Only character values are allowed for name. Please try again.")
        else: 
            name = name_input
            break

    age = None
    while True:
        age_input = input("Enter student age: ")
        if not age_input.isdigit():
            print("Error: Only numeric values are allowed for age. Please try again.")
        else:
            age = int(age_input)
            if age > 100:
                print("Error: Maximum age limit is 100. Please try again.")
            else:
                break

    grade = None 
    while True:
        grade_input = input("Enter student grade: ")
        if not grade_input.isalpha():
            print("Error: Only character values are allowed. Please try again.")
        else:            
            if len(grade_input) != 1:
                print("Invalid grade input.")
            else:
                grade = grade_input    
                break

    phone_number = None
    while True:
        phone_input = input("Enter student contact number (10 digits): ")
        if not phone_input.isdigit():
            print("Error: Only numbers are allowed. Please try again.")
        elif len(phone_input) != 10:
            print("Error: Mobile number must be exactly 10 digits. Please try again.")
        else: 
            phone_number = phone_input
            break

    qualifications = []
    while True:
        user_input = input("Do you want to add qualification (1: Yes || 0: No): ")
        if user_input == "1":        
            qualification_name = input("Enter your qualification: ")
            while True:
                passing_year = input("Enter your passing year: ")
                
                if not passing_year.isdigit():
                    print("Error: Passing year should contain only digits. Please try again.")
                else:
                    education = {
                        "Qualification name": qualification_name,
                        "Passing year": int(passing_year)
                    }
                    qualifications.append(education)
                    break
        elif user_input == "0":
            break
        else:
            print("Error: Please enter 1 for Yes or 0 for No.")


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
