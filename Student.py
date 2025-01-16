import json
import os

students = []
qualifications = [] 
counter = 0

while True:
    print("==========================================================")
    print(" Menu:")
    print("1. Enter student data")
    print("2. Display all student records")
    print("3. To find student records")
    print("4. Search Student by their Qualification ")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        num_students = int(input("Enter the number of students: "))
        for i in range(num_students):
            print("\nEnter details for student:")
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            mobile_no = int(input("Enter Your Mobile Number: "))
            grade = input("Enter student grade: ")

             

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
                'Mobile_Numeber': mobile_no,
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
        if counter == 0:
            print("No data is available.")
   
        else:
            path = os.getcwd() + "\\Data.json"
            with open(path, "r") as f:
                data = json.load(f)

            
            userinput=int(input("Enter the mobile number you want to search: "))
            find = False
            for student in data:
                if student["Mobile_Numeber"] == userinput:
                    print("Student Data: ", student) 
                    find = True                    
                    break

            if not find:
                print("No student found with this number.")
    
    elif choice == "4":
        if counter == 0:
            print("No data is available.")
   
        else:
            path = os.getcwd() + "\\Data.json"
            with open(path, "r") as f:
                data = json.load(f)

            
            userinput=(input("Enter Student Qualification to search: "))
            find = False
            for student in data:
                for Qualification in student["Qualifications"]:
                    if Qualification["qualification name"] == userinput:
                        print("Student Data: ", student) 
                        find = True                    
                        break

            if not find:
                print("No student found with this number.")
    
    elif choice == "5":
        print("\nExiting program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please enter 1, 2, 3, 4 or 5.")
        
