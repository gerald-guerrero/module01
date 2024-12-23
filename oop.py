class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."
    
alice = Person("Alice", 31)
print(alice.greet())

gerald = Person("Gerald", 25)
print(gerald.greet())

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name,age)
        self.student_id = student_id

bob = Student("Bob", 20, "1234")
print(bob.greet())
print(bob.student_id)

gerald = Student("Gerald", 25, "0000")
print(gerald.greet())
print(gerald.student_id)