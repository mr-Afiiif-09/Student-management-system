import json

#Defining class Student
class Student:

    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    
    def display(self):
        print(f"Name:{self.name}")
        print(f"Roll:{self.roll}")
        print(f"Marks:{self.marks}")

#Converting student object to dictionary 
    def to_dict(self):
        
        return {
            "name":self.name,
            "roll":self.roll,
            "marks":self.marks
        }

class StudentManager:
    def __init__(self):
        self.students = []
        self.load_student()

    def add_student(self,student):
        self.students.append(student)
        
    def view_students(self):
        if not self.students:
            print("No students record found")
            return

        for student in self.students:
            student.display()
            print("--------------")

    def search_student(self,roll):
        for student in self.students:
            if student.roll == roll:
                student.display()
                return
            
        print("Invalid roll number.Try again. ")

    def delete_student(self,roll):
        for student in self.students:
            if student.roll == roll:
                self.students.remove(student)
                print("Student deleted Successfully")
                return
              
        print("Invalid Roll number.Try again")

    def update_student(self,roll):
        for student in self.students:
            if student.roll == roll:
                roll = int(input("Enter New Roll:"))
                name = input("Enter New Name:")
                marks = float(input("Enter New marks:"))
                student.roll = roll
                student.name = name
                student.marks = marks
                print("Student Updated Successfully ")
                return
        
        print("Invalid roll number.Try again")
    
    def save_student(self):
        student_list = []
        for student in self.students:
            student_dict = student.to_dict()
            student_list.append(student_dict)
        with open("students_OOPS.json",'w') as f:
            json.dump(student_list,f,indent = 4)

    def load_student(self):
        try:
            with open("students_OOPS.json","r") as f:
                student_data = json.load(f)

            for student in student_data:
                student_obj = Student(
                    student["name"],
                    student["roll"],
                    student["marks"]
                )
                self.students.append(student_obj)
        except FileNotFoundError:
            self.students=[]

#Creating main function to run the program
def main():
    manager = StudentManager()

#Creating menu
    while True:
        print("========= Student Management System =========")
        print("1.Add Student")
        print("2.View Student")
        print("3.Search Student")
        print("4.Delete Student")
        print("5.Update Student")
        print("6.Exit")

        choice = input("Enter your choice:")

        if choice == '1':
            roll = int(input("Enter roll no:"))
            name = input("Enter Name:")
            marks = float(input("Enter marks:"))

            student = Student(name,roll,marks)
            manager.add_student(student)
            manager.save_student()
            print("Student Saved successfully")

        elif choice == '2':
            print("Student saved previously are:")
            manager.view_students()

        elif choice == '3':
            roll = int(input("Enter roll to search:"))
            manager.search_student(roll)

        elif choice == '4':
            roll = int(input("Enter roll to delete:"))
            manager.delete_student(roll)
            manager.save_student()

        elif choice == '5':
            roll = int(input("Enter roll to update:"))
            manager.update_student(roll)
            manager.save_student()

        elif choice == '6':
            print("Closing the program")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
            main()
    




    
    







