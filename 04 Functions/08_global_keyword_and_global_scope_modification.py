# ============================================================
# File: 08_global_keyword_and_global_scope_modification.py
# Chapter: 04 - Functions
# Topic: Using the global Keyword to Modify Global Variables
# ============================================================


# Problem Statement:

# Sometimes a function needs to modify a variable that
# exists in the global scope. By default, Python treats
# variables assigned inside a function as local.
#
# To modify a global variable from inside a function,
# Python provides the **global** keyword.



# Step 1: Global Variable
chai_type = "Plain"



# Step 2: Outer Function
def front_desk():

    # Step 3: Inner Function
    def kitchen():
        global chai_type
        chai_type = "Irani"

    kitchen()



# Step 4: Execute the Workflow
front_desk()



# Step 5: Check Updated Global Variable
print("Final global chai:", chai_type)



# Explanation:

# The variable 'chai_type' is defined in the global scope.
#
# Inside the kitchen() function, the 'global' keyword tells
# Python that we want to modify the global variable instead
# of creating a new local one.
#
# As a result, the value of 'chai_type' changes from
# "Plain" to "Irani", and the updated value is reflected
# outside the function as well.