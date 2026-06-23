# Lesson 1: Variables, Data Types, and Operators

def run_lesson():
    print("=" * 60)
    print("🌟 Lesson 1: Variables, Data Types, and Operators 🌟")
    print("=" * 60)
    
    # 1. Variables and Dynamic Typing
    print("\n1. Variables & Dynamic Typing:")
    print("   In Python, variables are dynamically typed. You don't need to declare their type.")
    
    name = "Python Developer"  # str
    age = 30                    # int
    height = 5.9                # float
    is_learning = True          # bool
    
    print(f"   name: {name} (Type: {type(name).__name__})")
    print(f"   age: {age} (Type: {type(age).__name__})")
    print(f"   height: {height} (Type: {type(height).__name__})")
    print(f"   is_learning: {is_learning} (Type: {type(is_learning).__name__})")

    # 2. Arithmetic & Logical Operators
    print("\n2. Operators:")
    a = 15
    b = 4
    print(f"   a = {a}, b = {b}")
    print(f"   Addition (a + b): {a + b}")
    print(f"   Division (a / b): {a / b}")
    print(f"   Floor Division (a // b): {a // b} (drops the decimal)")
    print(f"   Modulo (a % b): {a % b} (returns the remainder)")
    print(f"   Exponentiation (a ** b): {a ** b} (a raised to power of b)")

    # 3. Type Conversion (Casting)
    print("\n3. Type Casting:")
    str_num = "100"
    converted_num = int(str_num)
    print(f"   Converted '{str_num}' ({type(str_num).__name__}) to {converted_num} ({type(converted_num).__name__})")

    print("\n" + "=" * 60)
    print("📝 Mini-Challenge:")
    print("   Write a function 'convert_and_multiply(val_str, multiplier)' that:")
    print("   1. Converts 'val_str' to an integer.")
    print("   2. Multiplies it by the 'multiplier'.")
    print("   3. Returns the result.")
    print("=" * 60)

def convert_and_multiply(val_str, multiplier):
    # TODO: Implement this function!
    # Replace the pass statement with your logic
    return int(val_str) * multiplier

if __name__ == "__main__":
    run_lesson()
    
    # Test challenge
    assert convert_and_multiply("5", 10) == 50
    print("🎉 Challenge test passed successfully!")
