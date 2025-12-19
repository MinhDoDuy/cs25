s = input("Text: ").lower()

for ch in "x,?:.":
    s = s.replace(ch, " ")

words = s.split()

count = 0
for w in words:
    if w == "um":
        count += 1
print(f"Có {count} lần")
