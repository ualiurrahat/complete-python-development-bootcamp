
# Problem Statement:

# When working with nested functions, sometimes an inner
# function needs to modify a variable defined in the
# outer function.
#
# By default, Python treats variables inside a function
# as local. Therefore, the inner function cannot modify
# variables from the enclosing function directly.
#
# To solve this problem, Python provides the **nonlocal**
# keyword.
#
# The nonlocal keyword allows an inner function to modify
# variables defined in its enclosing (outer) function.




# Step 1: Global Variable
chai_type = "Ginger"   # Global scope



# Step 2: Outer Function

# This function defines a variable that belongs to the
# enclosing scope for the nested function.

def update_order():

    chai_type = "Elaichi"   # Enclosing scope variable

    print("Inside update_order() function - Chai type:", chai_type)


    # Step 3: Inner Function
    
    # The inner function wants to modify the variable from
    # the enclosing function.
    #
    # Without the 'nonlocal' keyword, Python would create
    # a new local variable instead of modifying the outer one.

    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"


    # Call the inner function
    kitchen()

    # The enclosing variable is now modified
    print("After kitchen() function update - Chai Order:", chai_type)



# Step 4: Execute the Function
update_order()



# Explanation:

# The **nonlocal keyword** allows an inner function to modify
# variables from the enclosing (outer) function.
#
# Scope hierarchy involved here:
#
# Global Scope:
#   chai_type = "Ginger"
#
# Enclosing Scope:
#   chai_type = "Elaichi" inside update_order()
#
# Local Scope:
#   variables inside kitchen()
#
# By using:
#
#     nonlocal chai_type
#
# the inner function kitchen() modifies the variable from
# the enclosing function instead of creating a new local one.
#
# This feature is useful when working with nested functions
# and closures where inner functions need to update values
# from their outer context.
