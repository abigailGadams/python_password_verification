from operator import itruediv
import string
import re # regular expression


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
    elif re.search("[\s]",password):
        print("Password should not contain any spaces")
        valid_password = False
           
    else:
        print('This password is valid!')
        valid_password = True
        return valid_password
            
       
            
       
# Main method
def main():
    password = input('Enter your new password: ')
    
      
    if (password_check(password)):
        print("Password is valid")
    else:
        print("Invalid Password !!")
          
# Driver Code        
if __name__ == '__main__':
    main()

