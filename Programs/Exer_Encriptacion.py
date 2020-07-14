import re
import crypt
#Create a code that asks for a password and if accepted it will be encrypted

#We create the function to make the encryption
def pw_crypt(pwaccepted):
  newpassword=crypt.crypt(pwaccepted,'salt')
  print()
  print("Encrypted password:",newpassword)
#We create the function to do the validation
def validation(password):
  if 6<= len(password) <=16:
    if re.search('[a-z]',password) and re.search('[A-Z]',password):
      if re.search('[.#_]',password):
        if re.search('[0-9]',password):
          print("Password accepted")
          pw_crypt(password)
        else:
          print("Password not accepted")
      else:
        print("Password not accepted")
    else:
       print("Password not accepted")
  else:
    print("Password not accepted")
#we ask the password
pw=input("Enter your password: ") #User part
#We pass the password
print(validation(pw)) #We use the function
