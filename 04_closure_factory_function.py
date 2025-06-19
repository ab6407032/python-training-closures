"""
Use Case: ✅ Factory Functions using Closures
--------------------------------------------
Closures allow you to generate customized functions with preset behavior.

🏭 Real-life Analogy:
A coffee shop lets you customize drinks. Once chosen, they remember your recipe.

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
