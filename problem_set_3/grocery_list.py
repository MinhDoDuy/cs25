#3 Grocery List
# items = {}
#
# while True:
#     try:
#         item = input().lower()
#         items[item] = items.get(item, 0) + 1
#     except EOFError:
#         break
#
# for item in sorted(items):
#     print(items[item], item.upper())