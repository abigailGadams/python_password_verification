from operator import itruediv
import string
import re # regular expression


# while True:
#   #Taking in password from user
#   user_input = input("Enter a password : ")
#   is_valid = False

#   if (len(user_input)<6 or len(user_input)>12):
#     #Check number of characters 
#     print("Not valid ! Total characters should be between 6 and 12")
#     continue
#   elif not re.search("[A-Z]",user_input):
#       #Check uppercase letter password requirement
#     print("Not valid ! It should contain one letter between [A-Z]")
#     continue
#   elif not re.search("[a-z]",user_input):
#     #Check lowercase letter password requirement
#     print("Not valid ! It should contain one letter between [a-z]")
#     continue
#   elif not re.search("[1-9]",user_input):
#     #7
#     print("Not valid ! It should contain one letter between [1-9]")
#     continue
#   elif not re.search("[~!@#$%^&*]",user_input):
#     #8
#     print("Not valid ! It should contain at least one letter in [~!@#$%^&*]")
#     continue
#   elif re.search("[\s]",user_input):
#     #9
#     print("Not valid ! It should not contain any space")
#     continue
#   else:
#     #10
#     is_valid = True
#     break

# if(is_valid):
#       print("Password is valid")


def password_check(password):

    Symbols =['$', '@', '#', '%', "!"]
    valid_password = True
        
    
    if not len(password) >= 6 and len(password) <= 16:
        print("Not valid ! Total characters should be between 6 and 12")
        valid_password = False
            
    elif not re.search('[a-z]',password):
        print('Password should include at least one lowercase letter')
        valid_password = False
            
    elif not re.search('[0-9]',password):
        print('Password should include at least one number')
        valid_password = False
           
    elif not re.search('[A-Z]',password):
        print('Password should include at least one uppercase letter')
        valid_password = False
            
    elif not any(char in Symbols for char in password):
        print('Password should have at least one of the symbols $@!#')
        valid_password = False  
           
    else:
        print('This password is valid!')
        valid_password = True
        return valid_password
            
       
            
       
# Main method
def main():
    password = input('Enter your new password: ')
    # passwd = 'Geek12@'
      
    if (password_check(password)):
        print("Password is valid")
    else:
        print("Invalid Password !!")
          
# Driver Code        
if __name__ == '__main__':
    main()

# import string
# import re # regular expression


# for letter in string.ascii_lowercase:
#     print(letter, end =" ")
# for letter in string.ascii_uppercase:
#     print(letter, end =" ")



# password = input('Enter your new password: ')
# characters = ['$','@','#']
# numbers = [range(0,9)]
# lowercase = string.ascii_lowercase 
# uppercase = string.ascii_uppercase


# def password_check(characters, numbers, lowercase,uppercase):
#     valid_password =  True # evaluates to 0
    
#     for i in password:
#         if len(password) < 6 | len(password>16):
#             i += 1
#         elif numbers not in password:
#             valid_password = False
#         elif lowercase not in password:
#             valid_password = False
#         elif uppercase not in password:
#             valid_password = False
#         else:
#             print('This password is valid!')
#             print(valid_password)
            
# password_check(password)
            