from classStudent import StudentManager
from exceptions import InvalidAgeError, StudentNotFoundError, ScoreError


def show_menu():
    print("\nMenu Student")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Top Student")
    print("4. List Student")
    print("5. Exit")

def input_name():
    while True:
        name = input("Student Name: ").strip().capitalize()
        if not name:
            print("❌ Name cannot be empty")
            continue
        if not all(c.isalpha() or c.isspace() for c in name):
            print("❌ Name only contains letters and spaces")
            continue
        name = " ".join(name.split())
        return name

def input_age():
    while True:
        try:
            age = int(input("Input Age: "))
            if age < 6 or age > 20:
                raise InvalidAgeError("❌ Age must be between 6 and 20")
            return age
        except ValueError:
            print("❌ Age must be a number")
        except InvalidAgeError as e:
            print(e)

def input_score():
    while True:
        try:
            score = float(input("Input Score: "))
            if score < 0 or score > 10:
                raise ScoreError("❌ Score must be between 0 and 10")
            return score
        except ValueError:
            print("❌ Score must be a number")
        except ScoreError as e:
            print(e)


def main():
    manager = StudentManager("student.csv")
    while True:
        show_menu()
        choice = input("Choose: ").strip()

        try:
            if choice == '1':
                name = input_name()
                age = input_age()
                score = input_score()

                manager.add_student(name, age, score)
                print("✅ Student added successfully")

            elif choice == '2':
                try:
                    students = manager.list_student()
                    if not students:
                        print("❌ Dont have any Student")
                    else:
                        for s in students:
                            print(
                                f"ID: {s.student_id} - {s.name} - {s.age} years old - Score: {s.score}đ - Rank: {s.get_rank()}")
                    student_id = int(input("Student ID to remove: "))
                    manager.remove_student(student_id)
                    print("✅ Student remove successfully")
                except ValueError:
                    print("❌ ID must be a number")
                except StudentNotFoundError as e:
                    print(e)

            elif choice == '3':
                top_student = manager.get_top_student()
                if not top_student:
                    print("❌ Dont have top student with score 8 or 10")
                else:
                    print("💯 Top student (>= 8): ")
                    for s in top_student:
                        print(
                            f"ID: {s.student_id} - {s.name} - {s.age} years old - Score: {s.score} - Rank: {s.get_rank()}")

            elif choice == '4':
                students = manager.list_student()
                if not students:
                    print("❌ Dont have any Student")
                else:
                    print("📶 List Student: ")
                    for s in students:
                        print(
                            f"ID: {s.student_id} - {s.name} - {s.age} years old - Score: {s.score}đ - Rank: {s.get_rank()}")
            elif choice == '5':
                print("\nBye")
                break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
