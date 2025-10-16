# Lesson 2 - Strings
# Worksheet 4
 
valid=0

def validate_username(username):
        if len(username) < 5 or len(username) > 15:
           valid = 0
        if not username[0].isalpha(): 
            valid = 0 
        if not username.isalnum(): 
            valid = 0
        valid=1
        return valid
    
    
    
for i in range(3):
    username = input ("print your username: ") 
    print(validate_username(username))
    if valid ==1:
        break
#print(validate_username("username"))    
#print(validate_username("username"))        
#print(validate_username("username"))   