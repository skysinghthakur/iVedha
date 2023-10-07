#Define a function that takes parameters and returns a value
def add(a,b):
    return a+b
#Above function take two integer/float value and return sum of those
val = add(8,5)
print(f"Value is {val}")

#Keyword Arguments
def ask1(name, question):
    print(f"Hello, {name}! {question}")

ask1(question="Have you interviewed at iVedha?", name="Akash")


#Default Argument
def ask2(name, question="Done with Assignment"):
    print(f"{question}, {name}!")

ask2("Akash")
ask2("Akash", "How are you?")




