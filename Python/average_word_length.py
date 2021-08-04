text = input()

words = text.split(" ")

print(words)

letters = [[l for l in word] for word in words]

counter = 0
for word in words:
    counter += len(word)

print(counter)

print(counter / len(words))
