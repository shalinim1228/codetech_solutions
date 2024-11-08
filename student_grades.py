# Function to convert letter grade to numeric grade
def letter_to_numeric(letter):
    letter = letter.upper()
    if letter == 'A':
        return 90
    elif letter == 'B':
        return 80
    elif letter == 'C':
        return 70
    elif letter == 'D':
        return 60
    elif letter == 'F':
        return 50
    else:
        return None  # Return None if the letter is invalid

# Function to calculate letter grade based on numeric average
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Function to calculate GPA based on average grade
def calculate_gpa(average):
    if average >= 90:
        return 4.0
    elif average >= 80:
        return 3.0
    elif average >= 70:
        return 2.0
    elif average >= 60:
        return 1.0
    else:
        return 0.0

# Main program function to manage student grades
def manage_student_grades():
    print("Welcome to the Student Grade Management System!")
    
    # Collect number of subjects/assignments
    num_subjects = int(input("Enter the number of subjects or assignments: "))
    
    grades = []
    subjects = []
    
    # Input grades for each subject or assignment
    for i in range(num_subjects):
        subject_name = input(f"Enter the name of subject/assignment #{i + 1}: ")
        
        # Ask for the grade and handle both numeric and letter inputs
        while True:
            grade_input = input(f"Enter the grade for {subject_name}: ").strip()
            
            try:
                # Check if the input is a valid numeric grade
                grade = float(grade_input)
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Please enter a grade between 0 and 100.")
            except ValueError:
                # If the input is not a valid number, check if it's a valid letter grade
                grade = letter_to_numeric(grade_input)
                if grade is not None:
                    grades.append(grade)
                    break
                else:
                    print("Invalid input. Please enter a valid numeric grade or letter grade (A, B, C, D, F).")
        
        subjects.append(subject_name)

    # Calculate average grade
    average = sum(grades) / len(grades)
    
    # Get letter grade and GPA
    letter_grade = get_letter_grade(average)
    gpa = calculate_gpa(average)
    
    # Display results
    print("\n===== Grade Summary =====")
    print("Subject/Assignment Grades:")
    
    for i in range(num_subjects):
        print(f"{subjects[i]}: {grades[i]}")

    print(f"\nAverage Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")
    
    if gpa >= 3.5:
        print("Excellent performance! Keep it up!")
    elif gpa >= 2.0:
        print("Good job! There's always room for improvement.")
    else:
        print("You might need to put in more effort. Don't give up!")

# Run the program
if __name__ == "__main__":
    manage_student_grades()
