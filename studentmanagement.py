FILE_NAME = "students.csv"

# ---------------- Student Class ----------------
class Student:
    def __init__(self, student_id, name, grade):
        self.id = student_id
        self.name = name
        self.grade = grade

    def to_csv(self):
        return self.id + "," + self.name + "," + self.grade

# ---------------- Manager Class ----------------
class StudentManager:
    def __init__(self):
        self.students = []
        self.load_students()

    # Load data from file
    def load_students(self):
        try:
            file = open(FILE_NAME, "r")
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    student = Student(parts[0], parts[1], parts[2])
                    self.students.append(student)
            file.close()
        except:
            pass   # file not found → ignore

    # Save data to file
    def save_students(self):
        file = open(FILE_NAME, "w")
        i = 0
        while i < len(self.students):
            file.write(self.students[i].to_csv() + "\n")
            i += 1
        file.close()

    # Check unique ID
    def is_unique_id(self, student_id):
        i = 0
        while i < len(self.students):
            if self.students[i].id == student_id:
                return False
            i += 1
        return True

    # Add student
    def add_student(self, student_id, name, grade):
        if not self.is_unique_id(student_id):
            print("ID already exists!")
            return

        student = Student(student_id, name, grade)
        self.students.append(student)
        self.save_students()
        print("Student added successfully!")

    # Update student
    def update_student(self, student_id, name, grade):
        i = 0
        while i < len(self.students):
            if self.students[i].id == student_id:
                self.students[i].name = name
                self.students[i].grade = grade
                self.save_students()
                print("Student updated!")
                return
            i += 1
        print("Student not found!")

    # Delete student
    def delete_student(self, student_id):
        i = 0
        while i < len(self.students):
            if self.students[i].id == student_id:
                self.students.pop(i)
                self.save_students()
                print("Student deleted!")
                return
            i += 1
        print("Student not found!")

    # List students
    def list_students(self):
        print("\n--- Student Records ---")
        print("ID\tName\tGrade")
        print("------------------------")

        i = 0
        while i < len(self.students):
            s = self.students[i]
            print(s.id + "\t" + s.name + "\t" + s.grade)
            i += 1

# ---------------- CLI Menu ----------------
def main():
    manager = StudentManager()

    while True:
        print("\n1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Enter ID: ")
            name = input("Enter Name: ")
            grade = input("Enter Grade: ")
            manager.add_student(sid, name, grade)

        elif choice == "2":
            sid = input("Enter ID to update: ")
            name = input("Enter New Name: ")
            grade = input("Enter New Grade: ")
            manager.update_student(sid, name, grade)

        elif choice == "3":
            sid = input("Enter ID to delete: ")
            manager.delete_student(sid)

        elif choice == "4":
            manager.list_students()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

# Run program
main()