def greet(name):
    return "Hello, " + name

print(greet("Alice"))

#this line is by mistake
def sec(func):
    return func

print(sec(greet)("Bob"))