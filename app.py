import json
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret"
DATA_FILE = Path(__file__).with_name("students_OOPS.json")


class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = int(roll)
        self.marks = float(marks)

    def to_dict(self):
        return {"name": self.name, "roll": self.roll, "marks": self.marks}


class StudentManager:
    def __init__(self):
        self.students = self.load_students()

    def load_students(self):
        if not DATA_FILE.exists():
            return []
        try:
            with DATA_FILE.open("r", encoding="utf-8") as file:
                records = json.load(file)
            return [
                Student(item["name"], item["roll"], item["marks"])
                for item in records
            ]
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            return []

    def save_students(self):
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump([student.to_dict() for student in self.students],
                      file, indent=4)

    def get_by_roll(self, roll):
        return next((student for student in self.students
                     if student.roll == roll), None)


def get_manager():
    return StudentManager()


@app.route("/")
def index():
    manager = get_manager()
    query = request.args.get("q", "").strip().lower()
    students = manager.students

    if query:
        students = [
            student for student in students
            if query in student.name.lower() or query in str(student.roll)
        ]

    total = len(manager.students)
    average = (
        sum(student.marks for student in manager.students) / total
        if total else 0
    )
    return render_template(
        "index.html",
        students=students,
        query=request.args.get("q", ""),
        total=total,
        average=average,
        editing=None
    )


@app.route("/add", methods=["POST"])
def add_student():
    name = request.form.get("name", "").strip()
    roll_text = request.form.get("roll", "").strip()
    marks_text = request.form.get("marks", "").strip()

    if not name or not roll_text or not marks_text:
        flash("Please fill in all fields.", "error")
        return redirect(url_for("index"))

    try:
        roll = int(roll_text)
        marks = float(marks_text)
        if roll < 0 or not 0 <= marks <= 100:
            raise ValueError
    except ValueError:
        flash("Enter a valid roll number and marks between 0 and 100.", "error")
        return redirect(url_for("index"))

    manager = get_manager()
    if manager.get_by_roll(roll):
        flash("That roll number already exists.", "error")
        return redirect(url_for("index"))

    manager.students.append(Student(name, roll, marks))
    manager.save_students()
    flash("Student added successfully.", "success")
    return redirect(url_for("index"))


@app.route("/edit/<int:roll>", methods=["GET", "POST"])
def edit_student(roll):
    manager = get_manager()
    student = manager.get_by_roll(roll)

    if not student:
        flash("Student record not found.", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        marks_text = request.form.get("marks", "").strip()

        try:
            marks = float(marks_text)
            if not name or not 0 <= marks <= 100:
                raise ValueError
        except ValueError:
            flash("Enter a name and marks between 0 and 100.", "error")
            return redirect(url_for("edit_student", roll=roll))

        student.name = name
        student.marks = marks
        manager.save_students()
        flash("Student updated successfully.", "success")
        return redirect(url_for("index"))

    return render_template(
        "edit.html",
        student=student
    )


@app.route("/delete/<int:roll>", methods=["POST"])
def delete_student(roll):
    manager = get_manager()
    student = manager.get_by_roll(roll)

    if not student:
        flash("Student record not found.", "error")
    else:
        manager.students.remove(student)
        manager.save_students()
        flash("Student deleted successfully.", "success")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
