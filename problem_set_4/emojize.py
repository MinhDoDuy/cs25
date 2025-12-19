import emoji

while True:
    text = input("Input Emoji: ")
    result = emoji.emojize(text, language="alias")

    if result != text:
        print(result)
        break
    else:
        print("Chưa in ra được emoji")
        print("Gợi í: :red_heart:\n")

