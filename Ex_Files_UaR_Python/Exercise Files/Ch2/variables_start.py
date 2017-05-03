# 
# Example file for variables
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
f = 0
print (f)

def someFunction():
    global f
    f = "def"
    print(f)

someFunction()
print(f)

