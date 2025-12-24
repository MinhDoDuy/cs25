from class1 import StudentManager
from exceptions import InvalidAgeError,StudentNotFoundError, ScoreError, DuplicateStudentIdError


def show_menu():
    print("\nMenu Student")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. List Student")
    print("4. Exit")

def main():
    class1 = StudentManager("data.csv")
    while True:
        show_menu()
        choice = input("Choose: ").strip()

        try:
            if choice == '1':
                #id
                while True:
                    try:
                        student_Id = int(input("Student ID: "))
                        if class1.is_exist(student_Id):
                            raise DuplicateStudentIdError
                        break
                    except ValueError:
                        print("❌ ID must be a number")
                    except DuplicateStudentIdError:
                        print("❌ ID Student already exists")
                        #phải cho except ở dưới để nhập lại luôn

                name = input("Student Name: ").capitalize()

                #age
                while True:
                    try:
                        age = int(input("Input Age: "))
                        if age < 10 or age > 20:
                            raise InvalidAgeError
                        break
                    except ValueError:
                        print("❌ Age must be number")
                    except InvalidAgeError:
                        print("❌ Age must be between 10 and 20")

                #score
                while True:
                    try:
                        score = float(input("Input Score: "))
                        if score < 0 or score > 10:
                            raise ScoreError
                        break
                    except ValueError:
                        print("❌ Score must be a number")
                    except ScoreError:
                        print("❌ Score must between 0 and 10")

                class1.add_student(student_Id, name, age, score)
                print("✅ Student add successfully")

            elif choice == '2':
                student_Id = int(input("Student ID: "))
                class1.remove_student(student_Id)
                print("✅ Product remove")

            elif choice == '3':
                students = class1.list_student()
                if not students:
                    print("❌ Dont have any student")
                for p in students:
                    print(f"Id: {p.student_Id} - {p.name} - {p.age} years old - {p.score}")

            elif choice == '4':
                print("\nBye")
                break
        except ValueError as e:
            print(e)
        except InvalidAgeError as e:
            print(e)
        except StudentNotFoundError as e:
            print(e)
        except ScoreError as e:
            print(e)
        except DuplicateStudentIdError as e:
            print(e)

if __name__ == "__main__":
    main()
