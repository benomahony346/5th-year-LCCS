# Lesson 1 - Strings
# Worksheet 2
# Tier 1: Complete tasks 1-5 - check answers
# Tier 2: Complete tasks 6-10 - check answers
# Tier 3: Complete tasks 11-13 - check answers

text = "Python Programming"

# Use your Reference Guide to help!

#
# Tier 1 - Complete Tasks 1-5
#

# 1. Convert to all uppercase
q1 = text.upper()
print(q1)
# 2. Convert to all lowercase  
q2 = text.lower()
print(q2)
# 3. Count how many times 'o' appears
q3 = text.count('o')
print(q3)
# 4. Replace 'Python' with 'Java'
q4 = text.replace('Python', 'Java')
print(q4)
# 5. Find the position where 'gram' starts
q5 = text.find('gram')
print(q5)
text = "Python Programming"

#
# Tier 2 - Complete Tasks 6-10
#

# 6. Check if the entire string is lowercase
q6 = text.islower()
print(q6)
# 7. Check if the entire string is uppercase
q7 = text.isupper()
print(q7)
# 8. Replace all spaces with underscores
q8 = text.replace(' ', '_')
print(q8)

# 9. Count how many times the letter 'P' appears (case-sensitive)
q9 = text.count("P")
print(q9)
# 10. Create a new string that says "I love Python Programming"
# Use .format() method
template = "I love {}"
q10 = template.format("Python Programming")
print(q10)

#
# Tier 3 - Complete Tasks 11-13
#

messy_input = "   PyThOn@123   "

# 11. Clean this input: remove spaces, make lowercase, 
# remove special characters
# You'll need multiple methods!
q11 = messy_input.lower().replace(" ","").replace("@","")
print(q11)
# 12. Check if a string contains ONLY letters (no numbers or spaces)
test_string = "PythonProgramming"

q12 = test_string.isalpha()
print(q12)
# 13. Create a function that takes any text and returns 
# the number of words (hint: count spaces + 1)
def countword