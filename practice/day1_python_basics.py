# Day 1 Practice — Python Basics

# 1. Program that takes user input (name, age) and prints formatted message
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}! You are {age} years old.")


# 2. Function that calculates factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Test factorial
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 7: {factorial(7)}")


# 3. Loop that prints multiplication table for a given number
def multiplication_table(n, limit=10):
    print(f"\nMultiplication table for {n}:")
    for i in range(1, limit + 1):
        print(f"{n} x {i} = {n * i}")


multiplication_table(5)


# 4. List of numbers — filter even ones into a new list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"\nOriginal list: {numbers}")
print(f"Even numbers: {even_numbers}")


# Additional practice: using dictionaries
person = {
    "name": "Subash",
    "age": 20,
    "city": "Salem"
}
print(f"\nDictionary example: {person}")
print(f"Person's name: {person['name']}")
