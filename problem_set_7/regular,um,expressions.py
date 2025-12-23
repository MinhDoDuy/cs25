import re

text = input("Text: ")
s = re.sub("[.?,:/]", " ", text.lower())

words = s.split()

count = 0
for w in words:
    if w == 'um':
        count += 1
print(f"Có {count} lần")
