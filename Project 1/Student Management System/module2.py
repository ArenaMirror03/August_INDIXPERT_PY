import json

def display_students(students):
    if not students:
        print("No records available.")
    else:
        print("\nStudent Records:")
        for student in students:
            print(json.dumps(student, indent=4))