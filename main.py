class Person:
    def __init__(self, fname, sname, age):
        self.firstname = fname
        self.secondname = sname
        self.age = age

    def __str__(self):
        return f"My name is {self.firstname} {self.secondname}"

parent = Person('John', 'Doe', 40)
print(parent)

class Student(Person):
    def __init__(self, fname, sname, age, student_id):
        super().__init__(fname, sname, age)
        self.student_id = student_id

    def __str__(self):
        return f"{super().__str__()} and I am a student with ID {self.student_id}"

x = Student('Mary', 'Doe', 22, 'S12345')
print(x)
