

import math


class MyException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class MyOperations:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            raise MyException(f"File '{self.filename}' not found.")

    def write_file(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)

    def square_root(self, num):
        return math.sqrt(num)

    def factorial(self, num):
        return math.factorial(num)

    def split_string(self, string, delimiter):
        return string.split(delimiter)

    def uppercase_string(self, string):
        return string.upper()
