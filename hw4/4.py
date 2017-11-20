print("variant:3")
with open("text.txt", encoding="utf-8") as f:
    text = f.read().split()
word_3 = 0
word_1 = 0
for word in text:
    word_3 += len(word) == 3
    word_1 += len(word) == 1
if word_1 == 0:
    print("No words with len 1")
else:
    print(word_3 / word_1)