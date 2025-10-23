#exercise2.3

sentence = input("please enter a sentence: ")
letter = input("please enter the letter you want to find: ")


count = 0

lower_sentence = sentence.lower()
lower_letter = letter.lower()

for i in lower_sentence :
    if i == lower_letter:
        count = count + 1

print("the letter apears", count, "times")