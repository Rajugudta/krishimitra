# Lesson 3: Functions and Modules

def run_lesson():
    print("=" * 60)
    print("🌟 Lesson 3: Functions and Modules 🌟")
    print("=" * 60)

    # 1. Defining and Calling Functions
    print("\n1. Function Basics:")
    def greet(name="User"):
        return f"Hello, {name}!"
    
    print(f"   Calling greet(): {greet()}")
    print(f"   Calling greet('Alice'): {greet('Alice')}")

    # 2. Arguments: positional, keyword, *args, **kwargs
    print("\n2. Arguments (*args, **kwargs):")
    
    def print_order(item, quantity=1, *notes, **customizations):
        print(f"   Item: {item}")
        print(f"   Quantity: {quantity}")
        if notes:
            print(f"   Notes: {notes}")
        if customizations:
            print(f"   Customizations: {customizations}")
            
    print_order("Espresso", 2, "Extra hot", "Use paper cup", milk="Almond", sweet="None")

    # 3. Importing Modules
    print("\n3. Using Built-in Modules:")
    import math
    print(f"   math.sqrt(16): {math.sqrt(16)}")
    print(f"   math.pi: {math.pi}")

    print("\n" + "=" * 60)
    print("📝 Mini-Challenge:")
    print("   Write a function 'build_profile(first, last, **info)' that:")
    print("   Returns a dictionary containing the keys 'first_name', 'last_name',")
    print("   and any other key-value pairs supplied in the keyword arguments.")
    print("=" * 60)

def build_profile(first, last, **info):
    # TODO: Implement this function!
    profile = {
        'first_name': first,
        'last_name': last
    }
    profile.update(info)
    return profile

if __name__ == "__main__":
    run_lesson()
    
    # Test challenge
    user_info = build_profile("John", "Doe", role="Developer", city="New York")
    assert user_info['first_name'] == "John"
    assert user_info['role'] == "Developer"
    print("🎉 Challenge test passed successfully!")
