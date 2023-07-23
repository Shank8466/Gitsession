# main.py

from assignment9 import MyOperations, MyException

if __name__ == "__main__":
    # File operations
    file_operations = MyOperations("example.txt")
    try:
        content = file_operations.read_file()
        print("File content:")
        print(content)
    except MyException as e:
        print(f"Error: {e}")

    file_operations.write_file("Hello, this is a test content.")

    # Mathematical operations
    math_operations = MyOperations("")
    print("Square root of 16:", math_operations.square_root(16))
    print("Factorial of 5:", math_operations.factorial(5))

    # String operations
    string_operations = MyOperations("")
    string_to_split = "This is a test string."
    print("Split string:", string_operations.split_string(string_to_split, " "))
    print("Uppercase string:", string_operations.uppercase_string(string_to_split))

    # Custom Exception
    try:
        raise MyException("This is a custom exception.")
    except MyException as e:
        print(f"Caught custom exception: {e}")
