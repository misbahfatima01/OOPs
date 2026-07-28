from person import Person, validate_string, validate_int

def validate_float(value, field):
    if not isinstance(value, (int, float)) or not (0.0 <= value <= 4.0):
        raise ValueError(f"{field} must be between 0.0 and 4.0")
    return float(value)

def validate_semester(value):
       if not isinstance(value, int) or not (1 <= value <= 8):
          raise ValueError("Semester must be between 1 and 8")
       return value

class Student(Person):
    def __init__(self, other=None, name=None, id=None, age=None, address=None, email=None,
                 student_id=None, rollno=None, program=None, department=None, semester=None, gpa=None):
        if isinstance(other, Student):  # Copy constructor
            super().__init__(other)
            self._student_id = other._student_id
            self._rollno = other._rollno
            self._program = other._program
            self._department = other._department
            self._semester = other._semester
            self._gpa = other._gpa
        else:
            super().__init__(name=name, id=id, age=age, address=address, email=email)
            self._student_id = validate_int(student_id, "Student ID")
            self._rollno = validate_string(rollno, "Roll No")
            self._program = validate_string(program, "Program")
            self._department = validate_string(department, "Department")
            self._semester = validate_int(semester, "Semester")
            self._gpa = validate_float(gpa, "GPA")

    @property
    def student_id(self):
        return self._student_id

    @property
    def rollno(self):
        return self._rollno

    @rollno.setter
    def rollno(self, value):
        self._rollno = validate_string(value, "Roll No")

    @property
    def program(self):
        return self._program

    @program.setter
    def program(self, value):
        self._program = validate_string(value, "Program")

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = validate_string(value, "Department")

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, value):
        self._semester = validate_int(value, "Semester")

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        self._gpa = validate_float(value, "GPA")

    def __str__(self):
        return (f"Student: {self.name}, Roll No: {self.rollno}, Dept: {self.department}, "
                f"Program: {self.program}, Semester: {self.semester}, GPA: {self.gpa}")

