#Exercise 9.1***********************************************

# Open the file grades.txt in write mode ('w') to store grades.
# If the file doesn't exist, it will be created. If it exists, it will be overwritten.
with open('grades.txt', 'w') as file:
    while True:
        # Prompt the user to enter a grade or -1 to stop
        grade = input("Enter a grade (or -1 to finish): ")
        
        # Check for the sentinel value to end input
        if grade == '-1':
            break
        
        # Write the grade to the file followed by a newline
        file.write(grade + '\n')

print("Grades have been written to grades.txt.")

#Exercise 9.2************************************************

# Open the grades.txt file in read mode ('r')
with open('grades.txt', 'r') as file:
    # Read all lines into a list, each line is a grade as a string
    grades = file.readlines()

# Initialize variables for total and count
total = 0
count = 0

print("Grades:")
# Loop through each grade in the list
for grade in grades:
    # Strip newline and whitespace, then convert to integer
    value = int(grade.strip())
    print(value)
    
    # Update the total and count
    total += value
    count += 1

# Compute the average
average = total / count if count > 0 else 0

print(f"\nTotal of {count} grades: {total}")
print(f"Average grade: {average:.2f}")

#Exercise 9.3************************************************

import csv
# Open the grades.csv file in write mode and use newline='' to avoid blank lines on Windows
with open('grades.csv', 'w', newline='') as file:
    # Create a csv.writer object to write rows to the CSV file
    writer = csv.writer(file)
    
    while True:
        # Ask the instructor if they want to add a new student
        cont = input("Enter a new student? (yes/no): ").strip().lower()
        if cont != 'yes':
            break
        
        # Prompt for student's first name, last name, and three exam grades
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")
        exam1 = int(input("Enter exam 1 grade: "))
        exam2 = int(input("Enter exam 2 grade: "))
        exam3 = int(input("Enter exam 3 grade: "))
        
        # Write a row in the format: firstname,lastname,exam1grade,exam2grade,exam3grade
        writer.writerow([firstname, lastname, exam1, exam2, exam3])

print("Student records have been written to grades.csv.")