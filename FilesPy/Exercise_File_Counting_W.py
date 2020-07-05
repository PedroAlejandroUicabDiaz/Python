#We are reading the file
with open('source.txt','r') as text:
  #We declarate our variables
  tab=0
  enter=0
  space=0
  words=0
  n_ch=0
  t_words=0;

  ch=text.read(1) #We assign character by character
  #It will work while it don't reach the end
  while(ch != ""): 
    if(ch=='\n'):
      enter=enter+1
    if(ch==' '):
      space=space+1
    if(ch=='\t'):
      tab=tab+1
    print(ch)
    words=words+1
    ch=text.read(1)

  print("----")
  print()
  #We show the counting 
  print("Tabs number:",tab)
  print("Enters number:",enter)
  print("Spaces number:",space)
  n_ch=(enter+space)
  t_words=(words-n_ch)
  print("Character total: ",t_words)
  print("Words number:",space*2)

"""
Link where it shows how to read and write in files:
https://www.youtube.com/watch?v=W0h-8sXlRJQ&t=121s 
"""
