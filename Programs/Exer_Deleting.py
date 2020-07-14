#Given a list of strings delete all special chars and numbers in each one.
#We create the function to find the characteres
def deleting_cha(string):
  valores = list([letra for letra in string
                if letra.isalpha()
                ])

  r = "".join(valores)
  print ("final string", r)

frase=input("Enter the string: ") #we show the string without special ch or numbers
deleting_cha(frase) #we pass our string
