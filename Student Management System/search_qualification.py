import json
import os

def search_by_qualification(students):
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