# Day 3 Practice — Python Advanced Basics

# 1. Exceptions — Division with error handling
def divide(a: float, b: float) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    finally:
        print("Division attempt completed.")
    return result


# Custom exception
class InvalidAgeError(Exception):
    """Raised when age is negative."""
    pass


def set_age(age: int) -> int:
    if age < 0:
        raise InvalidAgeError(f"Age cannot be negative: {age}")
    return age


# Test exceptions
print("=== Exception Tests ===")
print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")
try:
    set_age(-5)
except InvalidAgeError as e:
    print(f"Caught: {e}")
print(f"Age 25: {set_age(25)}")


# 2. Type Hints
def greet(name: str) -> str:
    return f"Hello, {name}!"


def get_numbers() -> list[int]:
    return [1, 2, 3, 4, 5]


print("\n=== Type Hint Tests ===")
print(greet("Subash"))
print(f"Numbers: {get_numbers()}")


# 3. List Comprehensions
squares = [x**2 for x in range(1, 11)]
print(f"\n=== List Comprehensions ===")
print(f"Squares 1-10: {squares}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers from {numbers}: {even_numbers}")


# 4. Dict Comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"\n=== Dict Comprehension ===")
print(f"Squares dict (1-5): {squares_dict}")


# 5. API Call with requests
import requests

print(f"\n=== API Call ===")
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"Status Code: {response.status_code}")
print(f"Response JSON: {response.json()}")

if response.status_code == 200:
    print("Request successful!")
else:
    print(f"Request failed with status: {response.status_code}")
