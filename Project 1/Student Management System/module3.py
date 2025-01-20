import json

def search_by_mobile(students):
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