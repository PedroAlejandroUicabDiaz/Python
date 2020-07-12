#Pedro Alejandro Uicab Diaz, Fixing the code 
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()  #Variable added
print("How much do you weight?", end=' ')  # ')' added
weight = input()

print("So, you're", age, "old", height, "tall and", weight, "heavy.")

script, filename = "argv" #("") added
#(filename) added
txt = open(filename)

print("Here's your file,{filename}:")
print(txt.read()) #(txt.read) added

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
#(txt_again) added 
print(txt_again())

# ("") added
print("Let's practice everything.")
#('') added
print('You\'d need to know \'bout escapes'
      'with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#(") added
print("--------------")
print(poem)
#() added
print("--------------")

#(6) added
five = 10 - 2 + 3 - 6
#")" added
print(f"This should be five: {five}")


#(:) added
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100  #(/) added
    return jelly_beans, jars, crates


start_point = 10000
#(crates) added
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print("We'd have",beans,"beans",jars,"jars and",crates,"crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) #(_)added
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

people = 20
#(cats) added
cats = 30
dogs = 15

#"()" added
if people < cats:
    print("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")
#(:) added
if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:  #(:) added
    #(") added
    print("People are less than or equal to dogs.")
# (== or is) added
if people == dogs:
    print("People are dogs.")
