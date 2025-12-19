#3 Just setting up my twttr
text = input("Text: ")
phim_bo = "ieaou"

result = ""
for c in text:
    if c not in phim_bo:
        result += c
print("Output:", result)