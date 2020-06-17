sentence=input("")
count = 0
for space in  sentence:
      if space == " ":
         count = count +1
print(f"Your sentence has [{count}] blank space ")
print(f"Here is your text:\n  {sentence}")
