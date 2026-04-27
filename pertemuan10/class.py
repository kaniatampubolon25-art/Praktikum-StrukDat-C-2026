class StackList:
  def __init__(self):
    self.items = [] # Menggunakan list bawaan Python

  def isEmpty(self):
   return len(self.items) == 0
  pass
  
  def push(self, url):
   self.items.append(url)
   pass

  def pop(self):
   if self.isEmpty():
    return "Riwayat kosong"
   return self.items.pop()
  pass
  
  def peek(self):
   if self.isEmpty():
    return "None"
   return self.items[-1]
  pass
  
  def size(self):
   return len(self.items)
  pass

# Create a stack
myStack = StackList()

myStack.push('https://edu.google.com/')
myStack.push('https://www.w3schools.com/')
myStack.push('https://classroom.google.com/')

print("Stack: ", myStack.items)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.items)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())