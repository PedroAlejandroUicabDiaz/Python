#Function to verify if the string is palindrome
def palindrome(phrase):
  phrase=phrase.lower()
  phrase=phrase.replace(' ', '')
  #If it is a pa or ca, return True
  return phrase==phrase[::-1]

s = input("Ingrese string: ")
#We show our string
print(s)
#We pass the string
print(palindrome(s))
#We are reading the file
with open('palindrome.txt','a') as sentence:
  #Condition to write  within our first file
  if(palindrome(s)==True):
    sentence.write(s)
    sentence.write('\n')
with open('Nonpalindrome.txt','a') as Sentence:
  #Condition to write within our second file
  if(palindrome(s)==False):
    Sentence.write(s)
    Sentence.write('\n')
#Message to verify that all ran well
print("Task Done")

"""
Link where shows how to read and write in files:
https://www.youtube.com/watch?v=W0h-8sXlRJQ&t=121s
"""
