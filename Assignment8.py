class A:
    def __init__(self, a_value, b_value, c_value):
        self.__a = a_value
        self._b = b_value
        self.c = c_value

    def display(self):
        print("Values in Class A:")
        print("a:", self.__a)   # Accessing private member (raises exception)
        print("b:", self._b)
        print("c:", self.c)

class B(A):
    def __init__(self, a_value, b_value, c_value):
        super().__init__(a_value, b_value, c_value)

    def display(self):
        print("Values in Class B:")
        # We can't directly access the private member '__a' from Class A in Class B
        # But we can access it using the protected member '_b' from Class A
        print("a (through _b):", self._b)
        print("c:", self.c)

try:
    # Creating an object of Class B
    obj_b = B(10, 20, 30)
    
    # Calling the display method of Class B
    obj_b.display()

except Exception as e:
    print("Exception occurred:", str(e))
    print("Rest of the code will continue executing.")






