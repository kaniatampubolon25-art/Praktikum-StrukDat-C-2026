stack = []

stack.append('https://edu.google.com/')
stack.append('https://www.w3schools.com/')
stack.append('https://classroom.google.com/')
print("Stack: ", stack)

topElement = stack[-1]
print("Peek: ", topElement)

poppedElement = stack.pop()
print("Pop: ", poppedElement)

print("Stack after Pop: ", stack)

is_empty = not bool(stack)
print("isEmpty: ", is_empty)

print("Size: ",len(stack))