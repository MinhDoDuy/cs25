# import cowsay
#
# # name = input("Nhập tên đi: ").upper()
# # cowsay.vader(f"{name}")
# print(cowsay.list_cows())
from os import name


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} in {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)



if __name__ == "__main__":
    main()
