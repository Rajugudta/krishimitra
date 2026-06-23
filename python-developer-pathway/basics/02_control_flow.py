# Lesson 2: Control Flow (Conditionals and Loops)

def run_lesson():
    print("=" * 60)
    print("🌟 Lesson 2: Control Flow (Conditionals and Loops) 🌟")
    print("=" * 60)

    # 1. Conditionals
    print("\n1. Conditionals (if, elif, else):")
    score = 85
    print(f"   Score = {score}")
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"   Resulting Grade: {grade}")

    # 2. Loops
    print("\n2. Loops:")
    print("   a) For Loop (iterating over a range):")
    print("      Printing numbers from 1 to 3:")
    for i in range(1, 4):
        print(f"         Iter: {i}")

    print("   b) While Loop (iterating while a condition is True):")
    count = 3
    while count > 0:
        print(f"         Count: {count}")
        count -= 1

    # 3. Loop Control
    print("\n3. Loop Control (break, continue):")
    print("   Skipping odd numbers and stopping at 8 in range(1, 10):")
    for n in range(1, 10):
        if n % 2 != 0:
            continue  # skip the rest of the loop block
        if n > 8:
            break     # terminate the loop
        print(f"      Even: {n}")

    print("\n" + "=" * 60)
    print("📝 Mini-Challenge:")
    print("   Write a function 'sum_even_numbers(n)' that:")
    print("   Calculates and returns the sum of all even numbers from 1 to 'n' (inclusive).")
    print("=" * 60)

def sum_even_numbers(n):
    # TODO: Implement this function!
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total

if __name__ == "__main__":
    run_lesson()
    
    # Test challenge
    assert sum_even_numbers(10) == 30  # 2 + 4 + 6 + 8 + 10 = 30
    print("🎉 Challenge test passed successfully!")
