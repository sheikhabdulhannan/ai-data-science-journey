text = 'python is easy'
print(text.title())

print(text.capitalize())

text = '    python is fun     '
print(text.strip())
print(text.rstrip())
print(text.lstrip())

name = 'ali'
print(name.isalpha())

namee = 'ali123'
print(namee.isalpha())

name = 'ahmed ali'
print(name.isalpha())

# ask user for a name . check if the name is valid

user = input('enter a name:')
print(user.isalpha())


value = '12344'
print(value.isdigit())

value ='1232sdew'
print(value.isdigit())

value = 12.3
print(value.isdigit())

usernamw = 'ahmed'
print(usernamw.isalnum())

isernamev = 'ahmed3_232'
print(isernamev.isalnum)

text = ' '
print(text.isspace())

name = 'python'
print(name.islower())

name  = 'AADA'
print(name.isupper())

name  = 'Python Programming'
print(name.istitle())


# ask user for a password
# if password cotain only letter print that
# is password contain only number print that
# if password contain  both, print password accepted
user = input('enter a password:')
if user.isalpha():
    print('only letter')
elif user.isdigit():
    print('only digit')
elif user.isalnum():
    print('accepted')
else:
    print('not accepted')        

text  = 'Python is easy and Python is powerfull'
print(text.rfind('is'))

filename = 'student.final.report.pdf' 
postion = filename.rfind('.')  
print(postion) 

extention = filename[postion+1:] 
print(extention)  

emial = 'abc@gmail.com'
result = emial.partition('@')
print(result)

# formatted string - fstring
name = 'ali'
age = 18
price = 500
qty = 3
print (f'total:{price* qty}')

average = 10/3
print(average)

print(f'{average:.1f}')

salary = 250000
print(f'salary:rs.{salary:,}')

filename = 'report_2026.pdf'
print(filename.startswith('report'))

print(filename.endswith('.pdf'))

# ask user for employee ID
# must start with
# remaining part must contain digits
# total lenght must be 8 characters
# sample employee ID : EMP1234

employee =input('what is your employee id:') 
if employee.startswith("EMP") and len(employee) == 8 and employee[3:].isdigit():
    print('valid id')
else:
    #print('invalid ID') 

# # Write a program to validate a specific format 
# of a vehicle license plate. The format requires:
# # • The first 3 characters must be alphabetic letters 
#  (uppercase or lowercase)
# # • The next character must be a hyphen (-)
# # • The last 3 characters must be digits
# # • Total length must be exactly 7 characters
# # • Sample Valid ID: ABC-123

plate = input('enter number plate:')      
if plate[:3].isalpha() and plate[3]== '-' and plate [4:].isdigit() and len(plate) == 7:
   print('valid plate')
else:
   print('invalid plate')    


username  = input('enter your id:')
if username[:3].isalpha() and username[3:].isdigit() and len(username)== 8:
    print('valid id')
else:
    print('invalid id ')    

# more
password = input('enter password:')
found_digit = False
for character in password:
    if character.isdigit():
         found_digit = True 
if found_digit and len(password) >= 8:
    print('valid')
else:
    print('invalid')             
    
            
