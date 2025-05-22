# Simple Calculator Project with Student List

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b

def main():
    students = []
    n = 0
    while n < 3 or n > 4:
        try:
            n = int(input("Enter number of students (3 or 4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        students.append(name)

    for student in students:
        print(f"\nCalculator for {student}:")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice (1/2/3/4): ")
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        print(f"Result for {student}: {result}")

if __name__ == "__main__":
    main()