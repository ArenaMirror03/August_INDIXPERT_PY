import json
import os

def register_students(students, file_path):
    
        print("\nEnter details for student:")
        student_id = None
        while True:
            student_input = input("Enter student ID: ")
            if student_input.isdigit():
                student_id = int(student_input)
                if any(student['Student ID'] == student_id for student in students):
                    print("Error: Student ID already exists. Please enter a different ID.")
                elif not student_input.isdigit():
                    print("Error: Only numbers are allowed for student ID. Please try again.")
                else: 
                    break
           
        
        
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
            if not age_input.isnumeric():
                print("Error: Only character values are allowed for name. Please try again.")
            else: 
                age = age_input
                break
   
        grade = None 
        while True:
            grade_input = input("Enter student grade: ")
            if not grade_input.isalpha():
                print("Error: Only character values are allowed. Please try again.")
            else: 
                grade = grade_input
                break

        phone_number = None
        while True:
            phone_input = input("Enter student contact number: ")
            if not phone_input.isdigit():
                print("Error: Only numbers. Please try again.")
            else: 
                phone_number = int(phone_input)
                break

        qualifications = []
        while True:
            user_input = input("Do you want to add a qualification (1: Yes || 0: No): ")
            
            if user_input == '0':
                break
            
            elif user_input == '1':
                qualification_name = input("Enter qualification name: ")
            passing_year = None
            while True:
                year_input = input("Enter passing year: ")
                if year_input.isdigit():
                    passing_year = int(year_input)
                    break
                else:
                    print("Error: Please enter Numeric Digits Only.")
                
                qualifications.append({
                    "Qualification name": qualification_name,
                    "Passing year": passing_year
                })
                
            


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