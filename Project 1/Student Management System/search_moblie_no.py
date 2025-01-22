import json

def search_by_mobile(students):
    if not students:
        print("No data is available.")
    else:
        while True:
            search_number = input("Enter the mobile number you want to search: ")
            if not search_number.isdigit():
                print("Error: Only digits are allowed. Please enter a valid mobile number.")
            else:
                break
        found = False
        for student in students:
            if student["Phone Number"] == search_number:
                print("Student found:", json.dumps(student, indent=4))
                found = True
                break
        if not found:
            print("No student found with this number.")