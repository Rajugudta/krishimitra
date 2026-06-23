# Lesson 5: File I/O and Exception Handling

import os
import json

def run_lesson():
    print("=" * 60)
    print("🌟 Lesson 5: File I/O and Exception Handling 🌟")
    print("=" * 60)

    # 1. Writing and Reading Text Files
    print("\n1. Writing and Reading Text Files:")
    filename = "sample_text.txt"
    
    # Writing
    with open(filename, "w") as f:
        f.write("Hello Python Developer!\nThis is a text file example.\n")
    print(f"   Written to {filename}")
    
    # Reading
    with open(filename, "r") as f:
        content = f.read()
    print("   File Content:")
    print(f"   {content.strip()}")
    
    # Clean up file
    if os.path.exists(filename):
        os.remove(filename)

    # 2. Working with JSON
    print("\n2. Working with JSON:")
    data = {
        "user": "Alice",
        "skills": ["Python", "FastAPI", "SQL"],
        "active": True
    }
    
    # Serializing JSON
    json_str = json.dumps(data, indent=2)
    print("   Serialized JSON string:")
    print(json_str)

    # 3. Exception Handling (try, except, finally)
    print("\n3. Handling Exceptions:")
    
    try:
        # Intentionally cause a ZeroDivisionError
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"   Caught Expected Error: division by zero ({e})")
    finally:
        print("   This 'finally' block always runs, whether an error occurred or not.")

    print("\n" + "=" * 60)
    print("📝 Mini-Challenge:")
    print("   Write a function 'safe_divide(a, b)' that:")
    print("   Attempts to divide 'a' by 'b'. If 'b' is 0, catches ZeroDivisionError")
    print("   and returns None. Otherwise, returns the quotient.")
    print("=" * 60)

def safe_divide(a, b):
    # TODO: Implement this function!
    try:
        return a / b
    except ZeroDivisionError:
        return None

if __name__ == "__main__":
    run_lesson()
    
    # Test challenge
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) is None
    print("🎉 Challenge test passed successfully!")
