"""
Use Case: ✅ Factory Functions using Closures
--------------------------------------------
Closures allow you to generate customized functions with preset behavior.

Context:
You are building a function generator that returns customized power functions. For example:

square = power_factory(2) returns a function that squares any number.

cube = power_factory(3) returns a function that cubes any number.

Each generated function should remember the exponent it was created with and apply it to the input number.

📌 Requirements:
Implement a factory function using closures that accepts an exponent and returns a new function.

The returned function should:

Accept a number x as input.

Return the result of x raised to the stored exponent.

Ensure that different returned functions retain their respective exponents independently.



"""

def power_factory(exponent):
    def power(x):
        return x ** exponent
    return power

# Create specialized power functions
square = power_factory(2)
cube = power_factory(3)

print(square(4))  # ➜ 16
print(cube(2))    # ➜ 8
