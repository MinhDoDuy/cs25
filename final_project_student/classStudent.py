import csv #Đọc file văn bản
from exceptions import InvalidAgeError, StudentNotFoundError, ScoreError


class Student:
    def __init__(self, student_Id, name, age, score):
        if age < 6 or age > 20:
            raise InvalidAgeError("Age must be between 10-20")
        if score < 0 or score > 10:
            raise ScoreError("Score must be between 0-10")
        self.student_Id = student_Id
        self.name = name
        self.age = age
        self.score = score

    def get_rank(self):
        if self.score >= 8:
            return "Very Good"
        elif self.score >= 6:
            return "Good"
        elif self.score >= 5:
            return "Fail "
        return "Below Average"


class StudentManager:
    def __init__(self, filename):
        self.filename = filename
        self.students = self.load_students() #Đọc file csv

    def load_students(self):
        students = []
        try:
            with open(self.filename, encoding="utf-8") as file:
                # with dùng để đảm bảo k hông bị leak tài dữ liệu ra ngoài và tự động đóng
                # encoding="" dùng để k bắt lỗi tiếng việt
                reader = csv.DictReader(file) #mỗi dòng là dict
                for row in reader:
                    students.append(
                        Student(
                            int(row["id"]),
                            row["name"],
                            int(row["age"]),
                            float(row["score"])
                        )
                    )
        except FileNotFoundError:
            pass
        return students

    def save_students(self):
        with open(self.filename, "w", newline='', encoding="utf-8") as file:
            # Mở file ở w
            # Mỗi lần ghi là xóa dữ liệu cũ ghi lại file vì ở đây chỉ xóa snapshot của self.students
            # Đảm bảo dữ liệu đồng bộ
            writer = csv.DictWriter(file, fieldnames=["id", "name", "age", "score", "rank"])
            writer.writeheader()
            for s in self.students:
                writer.writerow({
                    "id": s.student_Id,
                    "name": s.name,
                    "age": s.age,
                    "score": s.score,
                    "rank": s.get_rank()
                })

    def generate_id(self):
        if not self.students:
            return 1
        return max(s.student_Id for s in self.students) + 1

    def find_student_by_id(self, student_Id):
        for s in self.students:
            if s.student_Id == student_Id:
                return s
        raise StudentNotFoundError("❌ Student ID not found")

    def add_student(self, name, age, score):
        student_Id = self.generate_id()
        self.students.append(Student(student_Id, name, age, score))
        self.save_students()

    def remove_student(self, student_Id):
        student = self.find_student_by_id(student_Id)
        self.students.remove(student)
        self.save_students()

    def is_exist(self, student_Id):
        for s in self.students:
            if s.student_Id == student_Id:
                return True
        return False

    def get_top_student(self, min_score = 8):
        return [s for s in self.students if s.score >= min_score]

    def list_student(self):
        return sorted(self.students, key = lambda s: s.student_Id)
