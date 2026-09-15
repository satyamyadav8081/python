def add (x,y):
    return x + y
result=add(2,1)
print(result)

def greet():
    print("Hello, World!")
def display(other_def_func):
    print("this is display() function")
    other_def_func()
display(greet)        
