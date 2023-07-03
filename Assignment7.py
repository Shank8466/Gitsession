def append_data(roll_number, name, class_name, file="data.txt"):
    with open(file, "a") as f:
        f.write(f"Roll Number: {roll_number}\n")
        f.write(f"Name: {name}\n")
        f.write(f"Class: {class_name}\n")
    
    with open(file, "r") as f:
        data = f.readlines()
    
    print("Data in the file:")
    for line in data:
        print(line.strip())

# Example usage:
append_data("27", "Shashank Singh", "3rd year Diploma")