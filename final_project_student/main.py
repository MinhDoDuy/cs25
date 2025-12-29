from classStudent import StudentManager
from exceptions import InvalidAgeError, StudentNotFoundError, ScoreError


def show_menu():
    print("\nMenu Student")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. List Student")
    print("4. Top Student")
    print("5. Exit")

def main():
    manager = StudentManager("student.csv")
    while True:
        show_menu()
        choice = input("Choose: ").strip()

        try:
            if choice == '1':
                #id
                name = input("Student Name: ").capitalize().strip()

                #age
                while True:
                    try:
                        age = int(input("Input Age: "))
                        if age < 6 or age > 20:
                            raise InvalidAgeError("❌ Age must be between 6 and 20")
                        break
                    except ValueError:
                        print("❌ Age must be number")
                    except InvalidAgeError as e:
                        print(e)

                #score
                while True:
                    try:
                        score = float(input("Input Score: "))
                        if score < 0 or score > 10:
                            raise ScoreError("❌ Score must between 0 and 10")
                        break
                    except ValueError:
                        print("❌ Score must be a number")
                    except ScoreError as e:
                        print(e)

                manager.add_student(name, age, score)
                print("✅ Student add successfully")

            elif choice == '2':
                # student_Id = int(input("Student ID: "))
                # manager.remove_student(student_Id)
                # print("✅ Student remove successfully")
                try:
                    student_Id = int(input("Student ID: "))
                    manager.remove_student(student_Id)
                    print("✅ Student remove successfully")
                except ValueError:
                    print("❌ ID must be a number")
                except StudentNotFoundError as e:
                    print(e)

            elif choice == '3':
                students = manager.list_student()
                if not students:
                    print("❌ Dont have any Student")
                else:
                    print("📉 List Student: ")
                    for s in students:
                        print(f"Id: {s.student_Id} - {s.name} - {s.age} years old - Score: {s.score}đ")

            elif choice == '4':
                top_student = manager.get_top_student()
                if not top_student:
                    print("❌ Dont have top student with score 9 or 10")
                else:
                    print("💯 Top student (>= 9): ")
                    for s in top_student:
                        print(f"Id: {s.student_Id} - {s.name} - {s.age} years old - Score: {s.score}")

            elif choice == '5':
                print("\nBye")
                break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
