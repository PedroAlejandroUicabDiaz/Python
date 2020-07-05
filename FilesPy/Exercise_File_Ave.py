#We are reading the file
with open('number_list.txt','r') as n_list:
  #We declarate our variables
  suma=0
  average=0
  count=0
  #We assig number by number
  numbers=n_list.readline()
  while(numbers):
    suma=suma+float(numbers)
    numbers=n_list.readline()
    count=count+1

  print()
  #we realize the average
  average=(suma/count)
  #we show it
  print("The average is:",average)

"""
Link where shows how to read and write in files:
https://www.youtube.com/watch?v=W0h-8sXlRJQ&t=121s 
"""
