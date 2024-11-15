# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Ericka Moreno, 11/13/24, Began assignment 05 script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str,str] = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
parts:list[str]


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    for row in file.readlines():
        # Transform the data from the file
        parts = row.strip().split(',')
        student_first_name = parts[0]
        student_last_name = parts[1]
        course_name = parts[2]
        student_data = {'first_name':student_first_name,'last_name':student_last_name,'course_name':course_name}
        # Load it into our collection (list of lists)
        students.append(student_data)
    file.close()
    print(students)
# Handle the case where the specified file does not exist by catching the FileNotFoundError
except FileNotFoundError as e:
    print('Text file not found')
    print('---Technical Information---')
    print(e, e.__doc__, type(e), sep='\n')
    print("creating file since it doesn't exist")
    open(FILE_NAME, "w")
finally:
    if not file.closed:
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            # Check that first name contains alphabetic characters only
            if not student_first_name.isalpha():
                raise ValueError('First name must be alphabetic')
            student_last_name = input("Enter the student's last name: ")
            # Check that last name contains alphabetic characters only
            if not student_last_name.isalpha():
                raise ValueError('Last name must be alphabetic')
            course_name = input("Please enter the name of the course: ")
            student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course_name': course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print (e)

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        # For each individual student in students list, format the data into a sentence and print it out
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            # For each student in the students list, write their first name, last name, and course name into JSON file
            file = open(FILE_NAME, "w")
            for student in students:
                csv_data = f"{student['first_name']},{student['last_name']},{student['course_name']}\n"
                file.write(csv_data)
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        # Catch error in saving data to JSON file
        except Exception as e:
            print('Error saving data to file')
            print(e)
        finally:
            if file and not file.closed:
                file.close()


    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
