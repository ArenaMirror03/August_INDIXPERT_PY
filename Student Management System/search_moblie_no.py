import json
import os

def search_by_mobile(students):
    if not students:
        print("No data is available.")
        return  

    while True:
        search_number = input("Enter the mobile number you want to search  ")

        if search_number and not search_number.isdigit():  
            print("Error: Only digits are allowed. Please enter a valid mobile number.")
        elif not search_number:
            print("You must enter a mobile number to search.")  
        else:
            break  
    
    
    if search_number:
        found = False
        for student in students:
            if str(student["Phone Number"]) == search_number:  
                print("Student found:", json.dumps(student, indent=4))
                found = True
                break
        
        if not found:
            print("No student found with this number.")  
