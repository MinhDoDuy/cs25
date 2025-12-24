import csv #Đọc file văn bản

from exceptions import InvalidAgeError, StudentNotFoundError, ScoreError


class Student:
    def __init__(self, student_Id, name, age, score):
        if age < 10 or age > 20:
            raise InvalidAgeError("Age must be between 10-20")
        if score < 0 or score > 10:
            raise ScoreError("Score must be between 0-10")
        self.student_Id = student_Id
        self.name = name
        self.age = age
        self.score = score


class StudentManager:
    def __init__(self, filename):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        students = []
        try:
            with open(self.filename, encoding="utf-8") as file:
                # with dùng để đảm bảo k hông bị leak tài dữ liệu ra ngoài
                # encoding="" dùng để k bắt lỗi tiếng việt

                reader = csv.DictReader(file)
                for row in reader:
                    students.append(
                        Student(int(row["id"]), row["name"], int(row["age"]), float(row["score"]))
                    )
        except FileNotFoundError:
            pass
        return students

    def save_students(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            # Mở file ở w
            # Mỗi lần ghi là xóa dữ liệu cũ ghi lại file vì ở đây chỉ xóa snapshot của self.students
            # Đảm bảo dữ liệu đồng bộ
            writer = csv.DictWriter(file, fieldnames=["id", "name", "age", "score"])
            writer.writeheader()
            for p in self.students:
                writer.writerow({
                    "id": p.student_Id,
                    "name": p.name,
                    "age": p.age,
                    "score": p.score
                })

    def add_student(self, student_Id, name, age, score):
        # for s in self.students:
        #     if s.student_Id == student_Id:
        #         raise ValueError("ID Student already exists")
        self.students.append(Student(student_Id, name, age, score))
        self.save_students()

    def is_exist(self, student_Id):
        for s in self.students:
            if s.student_Id == student_Id:
                return True
        return False

    def remove_student(self, student_Id):
        for p in self.students:
            if p.student_Id == student_Id:
                self.students.remove(p)
                self.save_students()
                return
        raise StudentNotFoundError("Student not found")

    def list_student(self):
        return self.students
