import re

#We create a function to do the validation
def validation(password):
  if 6<= len(password) <=16: #Fisrt condition
    if re.search('[a-z]',password) and re.search('[A-Z]',password): #Second Condition
      if re.search('[.#_]',password): #Third condition
        if re.search('[0-9]',password): #Forth condition
          print("Password accepted")
        else:
          print("Password not accepted")
      else:
        print("Password not accepted")
    else:
       print("Password not accepted")
  else:
    print("Password not accepted")

pw=input("Enter your password: ") #User part
print(validation(pw)) #We use the function

#Help from John Ortiz Ordonez
