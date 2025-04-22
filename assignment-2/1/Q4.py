words = []
while True:
    word = input("Enter a word (blank to stop): ")
    if word == "":
        break
    if word not in words:
        words.append(word)

for word in words:
    print(word)