class Bias:
    def __init__(self, name, group , age):
        self.name = name
        self.group = group
        self.age = age

    def greet(self):
        print("Hello, my bias is " + self.name)

    def change_age(self,new_age):
        self.age = new_age
        print(f"he is {self.age} years old now")

p1 = Bias("Budi", "EXO", 30)
p2 = Bias("Dimas", "NCT", 25)
p3 = Bias("Ayu", "REDVELVET", 28)

print(p1.name, p1.group, p1.age)
print(p2.name, p2.group, p2.age)
print(p3.name, p3.group, p3.age)

p1.greet()
p1.change_age(31)

        

