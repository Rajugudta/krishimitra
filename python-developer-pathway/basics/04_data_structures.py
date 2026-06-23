# Lesson 4: Data Structures (Lists, Tuples, Dictionaries, Sets)

def run_lesson():
    print("=" * 60)
    print("🌟 Lesson 4: Data Structures (Lists, Tuples, Dicts, Sets) 🌟")
    print("=" * 60)

    # 1. Lists
    print("\n1. Lists (Ordered, mutable):")
    fruits = ["apple", "banana"]
    fruits.append("cherry")
    print(f"   Fruits list: {fruits}")
    print(f"   First element: {fruits[0]}")
    print(f"   Last element: {fruits[-1]}")
    
    # 2. Tuples
    print("\n2. Tuples (Ordered, immutable):")
    coordinates = (10, 20)
    print(f"   Coordinates tuple: {coordinates}")
    # coordinates[0] = 15  # This would raise TypeError!

    # 3. Dictionaries
    print("\n3. Dictionaries (Key-Value pairs):")
    student = {"name": "Alice", "age": 22, "major": "Computer Science"}
    print(f"   Student dict: {student}")
    print(f"   Student's name: {student['name']}")
    student["age"] = 23  # mutable
    print(f"   Updated student: {student}")

    # 4. Sets
    print("\n4. Sets (Unordered, unique values):")
    colors = {"red", "blue", "green", "red"}  # duplicates are automatically removed
    print(f"   Colors set: {colors}")
    colors.add("yellow")
    print(f"   Is 'blue' in set? {'blue' in colors}")

    # 5. List Comprehensions
    print("\n5. List Comprehensions:")
    numbers = [1, 2, 3, 4, 5]
    squares = [n**2 for n in numbers if n % 2 != 0]
    print(f"   Odd squares of {numbers}: {squares}")

    print("\n" + "=" * 60)
    print("📝 Mini-Challenge:")
    print("   Write a function 'count_words(word_list)' that:")
    print("   Takes a list of strings and returns a dictionary with the count of each string.")
    print("=" * 60)

def count_words(word_list):
    # TODO: Implement this function!
    counts = {}
    for word in word_list:
        counts[word] = counts.get(word, 0) + 1
    return counts

if __name__ == "__main__":
    run_lesson()
    
    # Test challenge
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    result = count_words(words)
    assert result["apple"] == 3
    assert result["banana"] == 2
    assert result["cherry"] == 1
    print("🎉 Challenge test passed successfully!")
