import json
import os

def register_students(students, file_path):
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
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