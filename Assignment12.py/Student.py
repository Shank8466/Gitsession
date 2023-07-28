class Students:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Roll Number: {self.roll_number}"
