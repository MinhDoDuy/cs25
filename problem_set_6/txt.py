# # name = input("What your name: ")
# #
# # with open("before.csv", "a") as file:
# #     file.write(f"{name}\n")
# from os import name
#
# # with open("before.csv") as file:
# #     for line in sorted(file):
# #         print("Hello,", line.rstrip())
#
# # names = []
# # with open("before.csv") as file:
# #     for line in file:
# #         names.append(line.rstrip())
# # for name in sorted(names, reverse=True):
# #     print(f"hello, {name}")
#
with open("before.csv") as file:
    for line in file:
        lastname, firstname, house = line.rstrip().split(",")
        print(f"{firstname} {lastname}, is in {house}")
#
# students = []
# with open("before.csv") as file:
#     for i in file:
#         name, house = i.rstrip().split(",")
#         # students.append(f"{name} is in {house}")
# # for s in sorted(students):
# #     print(s)
# #         s = {}
# #         s["name"] = name
# #         s["house"] = house
#         s = {"name": name, "house": house}
#         students.append(s)
#
# for s in students:
#     print(f"{s['name']} is in {s['house']}")

