from student import Student
from student_list import StudentList

def main():
    student_list = StudentList()

    s1 = Student(name="Ali", id=1, age=20, address="Lahore", email="ali@gmail.com",
                 student_id=101, rollno="B24110002456", program="BSCS", 
                 department="Computer Science",semester=4, gpa=3.6)

    s2 = Student(name="Sara", id=2, age=21, address="Karachi", email="sara@gmail.com",
                 student_id=102, rollno="B24110001569", program="BSCS", 
                 department="Computer Science",semester=5, gpa=3.4)

    s3 = Student(name="Bilal", id=3, age=19, address="Islamabad", email="bilal@gmail.com",
                 student_id=103, rollno="B24110006078", program="BSSE", 
                 department="Software Engineering",semester=2, gpa=3.9)
    

    # Add students to the list
    print("\nAdding students...")
    student_list.add_student(s1)
    student_list.add_student(s2)
    student_list.add_on(s3, 1)   # Add Bilal in the middle

    # Display all students
    print("\n--- current Student List ---")
    student_list.display()

    # Search student by name
    print("\nSearching for 'Sara':")
    results = student_list.search_student("Sara")
    for r in results:
        print(r)

    # Search student by ID
    print("\nSearching for ID 103:")
    results = student_list.search_student(103)
    for r in results:
        print(r)

    # Update student record
    print("\nUpdating Sara’s record...")
    updated_student = Student(name="Sara", id=2, age=21, address="Karachi", email="sara@gmail.com",
                       student_id=102, rollno="B24110001569", program="BSCS", 
                       department="Computer Science",semester=6, gpa=4.0)
    student_list.update_student(102, updated_student)

    print("\n--- After Update ---")
    student_list.display()
    
    # Remove student
    print("\nRemoving student with ID 101...")
    student_list.remove_student(101)

    # Final display
    print("\n--- Final Student List ---")
    student_list.display()


if __name__ == "__main__":
    main()
