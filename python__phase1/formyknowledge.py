import json
import os

students = []
counter=0

while True:
    print("==========================================================")
    print(" Menu:")
    print("1. Enter student data")
    print("2. Display all student records")
    print("3. For searching the data using mobile number")
    print("4. For searching the data using qualification")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1": 
          
            print("\nEnter details for student:")
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ") 
            phone_number = int(input("Enter your mobile number: "))
            
            qualifications = []
            while True:
                userinput=int(input("Do you want to add qualification(1: Yes || 0: No): "))
                if userinput==1:
                    education = {}
                    education["Qualification name"] = input("Enter your qualication: ")
                    education["Passing year"] = int(input("Enter your passing year: "))
                    qualifications.append(education)
                else:
                    break    

            students.append({
                'Student ID': student_id,
                'Name': name,
                'Age': age,
                'Grade': grade,
                'phone number':phone_number,
                'qualification': qualifications
            })
            counter=1

    elif choice == "2":
        if counter == 0:
            print("The list is empty.")

        else:
            path = os.getcwd()+"\\jsondata.json"
            with open(path,"a") as f:
                f.write(json.dumps(students,indent=4))
            print("The json file is created")

    elif choice == "3":
        if counter == 0:
            print("No data is available.")
   
        else:
            path = os.getcwd() + "\\jsondata.json"
            with open(path, "r") as f:
                data = json.load(f)
            
            userchoice=int(input("Enter the mobile number you want to search: "))
            find = False
            for student in data:
                if student["phone number"] == userchoice:
                    print("Student found: ", student) 
                    find = True                    
                    break

            if not find:
                print("No student found with this number.")

    elif choice == "4":
        
        if counter == 0:
            print("No data is available.")
        else:
            path = os.getcwd() + "\\jsondata.json"
            with open(path, "r") as f:
                data = json.load(f)
            
            user_qualification = input("Enter the qualification you want to search: ")
            find = False
            for student in data:
                for qualify in student["qualification"]:
                    if qualify["Qualification name"].lower() == user_qualification.lower():  
                        print("Student found: ", student) 
                        find = True                    
                        break

            if not find:
                print("No student found with this qualification.")

            
    elif choice == "5":
        print("\nExiting program. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter 1, 2, 3, 4 or 5.")