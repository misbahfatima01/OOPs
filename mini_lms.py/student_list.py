from student import Student
class StudentList:
    def __init__(self, capacity=3):
        self._students = []
        self._size = 0
        self._capacity = capacity

    def expand_list(self):
        self._capacity *= 2
        print(f"List expanded! New capacity: {self._capacity}")

    def add_student(self, student):
        if self._size >= self._capacity:
            self.expand_list()
        for s in self._students:
            if s.student_id == student.student_id:
                raise ValueError(f"Student with ID {student.student_id} already exists")
        self._students = self._students + [student]
        self._size += 1
        print(f"Student '{student.name}' added successfully at the end.")

    def add_on(self, student, position):
        if self._size >= self._capacity:
            self.expand_list()
        if position < 0 or position > len(self._students):
            raise IndexError("Invalid position")
        self._students = self._students[:position] + [student] + self._students[position:]
        self._size += 1

    def search_student(self, key):
        if isinstance(key, int):
            return [s for s in self._students if s.student_id == key]
        elif isinstance(key, str):
            return [s for s in self._students if key.lower() in s.name.lower()]
        else:
            raise TypeError("Search key must be name (str) or student ID (int)")

    def update_student(self, student_id, new_student):
        for student in self._students:
          if student.student_id == student_id:
            student.name = new_student.name
            student.email = new_student.email
            student.rollno = new_student.rollno
            student.program = new_student.program
            student.semester = new_student.semester
            print(f"Student with ID {student_id} updated.")
            return True

        print(f"Student with ID {student_id} not found.")
        return False


    def remove_student(self, keyword):
        for i in range(self._size):
          student = self._students[i]
          if student.student_id == keyword or student.name.lower() == str(keyword).lower():
            print(f"Removing student: {student.name} (ID: {student.student_id})")
            self._students = self._students[:i] + self._students[i+1:]
            self._size -= 1
            print("Student removed successfully.")
            return True

        print(f"No student found for '{keyword}'.")
        return False


    def display(self):
        if not self._students:
            print("No students in the list.")
        else:
            print("\n--- Student Records ---")
            for s in self._students:
                print(s)


