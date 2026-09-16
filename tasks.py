
# userList = []
# 
# userName = input("Enter your name: ")
# userList.append(userName)
# 
# userAge = int(input("What age are you " + userName + "?"))
# userList.append(userAge)
# 
# userCountry = input("What is your country of birth?")
# userList.append(userCountry)
# 
# userYear = int(input("What year were you born?"))
# userList.append(userYear)
# 
# print("My database for " + userName + "\n" + str(userList))
# 
# print(userList[::-1])

words = "The five boxing wizards jump quickly".split()

print(words)

word1 = words.pop()
word2 = words.pop()

word3 = words.pop(0)
word4 = words.pop(0)
word5 = words.pop(0)
word6 = words.pop(0)

print(word1.capitalize(), word2, word3.lower(), word4, word5, word6)