# def validate(ip):
#     parts = ip.split(".")
#
#     if len(parts) != 4:
#         return False
#
#     for p in parts:
#         if not p.isdigit():
#             return False
#         number = int(p)
#         if number < 0 or number > 255:
#             return False
#     return True
#
# if __name__ == "__main__":
#     print(validate("127.0.0.1"))
#     print(validate("256.1.1.1"))
#     print(validate("1.2.3.4"))