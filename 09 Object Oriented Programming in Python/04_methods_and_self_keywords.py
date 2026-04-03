"""
File: 04_methods_and_self_keyword.py
Chapter: Object Oriented Programming In Python
Topic: Instance Methods and the Role of 'self'
Problem Statement:
Understand how methods work inside a class and why the 'self' parameter
is required. Learn how methods are called using objects and how calling
a method using the class requires explicitly passing the object.
"""

# ---------------------- Step 1: Defining a Class with a Method ----------------------
class Teacup:
    size = 150  # ml (class attribute)

    # Instance Method
    # 'self' represents the object that is calling this method.
    # Using 'self', attributes and other methods of the class can be accessed.
    def describe(self):
        return f"A {self.size} ml chai cup"


# ---------------------- Step 2: Calling Method Using an Object ----------------------
cup = Teacup()

# When called using the object, Python automatically passes the object
# as the first argument to the method (self).
print(cup.describe())


# ---------------------- Step 3: Calling Method Using the Class ----------------------
# If the method is called using the class name,
# Python does NOT know which object should be passed as 'self'.
# So calling like below will raise an error:
# Teacup.describe()

# Correct way: explicitly pass the object as the first argument
print(Teacup.describe(cup))


# ---------------------- Step 4: Object-Specific Attribute Change ----------------------
# Creating another object
cupTwo = Teacup()

# Changing size only for this object (object namespace)
cupTwo.size = 100

# Passing this object explicitly to the class method
print(Teacup.describe(cupTwo))