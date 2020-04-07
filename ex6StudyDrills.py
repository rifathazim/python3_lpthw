types_of_people = 10 #initialization
x = (f"There are {types_of_people} types of people.") #string formatting

do_not = "don't"
binary1 = "binary" #initialization
y = (f"Those who know {binary1} and those who {do_not}.") #string formatting

print(x) #printing
print(y) #printing

print(f"I said: {x}") #printing string using formatting
print(f"I also said: '{y}'")#printing string using formatting

hilarious = True #initialization(boolean)
joke_evaluation =  ("Isn't that joke so funny?! {} ") #initialization, here a scope for a string

print(joke_evaluation.format(hilarious)) #another string formatting method

w = "This is the left side of…" #string initialization
e ="a string with a right side." #string initialization

print(w + e) #string cascading