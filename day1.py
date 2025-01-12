students = []

while True:
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

            
            students.append({
                'Student ID': student_id,
                'Name': name,
                'Age': age,
                'Grade': grade
            })

    elif choice == "2":
        print("\nStudent Data:")
        print(students)  
        
    elif choice == "3":
        print("\nExiting program. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.")