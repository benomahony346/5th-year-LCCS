# reshearch project 

# number one . repalce
# this pice of code replaces the given string with what you put in there
example = "Coding is the best"
print(example)
print(example.replace("Coding", "Maths")) #in this case i switched the subject

# number two .lower and .upper
# theses peices of code check your string if its all lower case or all uppercase
#i will use adiffrent example
example1 = "i like basketball"
print(example1.islower()) # its true as the text is all lower case 
print(example1.isupper()) # this says false because it isnt all upper case

#number 3 . is alpha
#this piece of code checks if the string is just letters 
example2 = "I am 17 years old"
example3 = "Iamseventeenyearsold"
print(example2)
print(example2.isalpha())
print(example3)
print(example3.isalpha())

#number4 .isdigit
#this checks if the code is just numbers
example4 = "1234567890"
example5 = "one 234567890"
print(example4)
print(example4.isdigit())
print(example5)
print(example5.isdigit())