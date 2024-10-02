import os
import random
import time

def insecure_file_handling(filename):
    """
    This function demonstrates insecure file handling.
    """
    # Security risk: Potential path traversal vulnerability
    with open(filename, 'r') as f:
        content = f.read()
    return content

def performance_hog(n):
    """
    This function has intentional performance issues.
    """
    # Performance issue: Inefficient list creation
    result = []
    for i in range(n):
        result = result + [i]
    return result

class PoorlyDocumentedClass:
    """A class with various issues."""
    
    def __init__(self, x):
        self.x = x
    
    def poorly_named_method(self):
        # Styling issue: Inconsistent naming convention
        return self.x * 2
    
    def potential_division_by_zero(self, y):
        # Common bug: Potential division by zero
        return self.x / y

def unused_import_and_variable():
    # Unused import (os) and unused variable
    unused_var = 42
    return random.randint(1, 10)

def global_variable_abuse():
    global some_global
    some_global = "This is a global variable"
    
    def nested_function():
        # Bug: Modifying a global variable in a nested function
        global some_global
        some_global += " modified"
    
    nested_function()
    return some_global

def resource_leak():
    # Resource management issue: File not properly closed
    f = open("temp.txt", "w")
    f.write("This file may not be closed properly")

def infinite_recursion(n):
    # Common bug: Infinite recursion
    if n == 0:
        return 0
    return 1 + infinite_recursion(n)  # Missing base case


def sql_injection_vulnerability(user_id):
    """
    This function demonstrates a SQL injection vulnerability.
    """
    # Security risk: SQL injection
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()

def hardcoded_password():
    """
    This function uses a hardcoded password.
    """
    # Security risk: Hardcoded credentials
    username = "admin"
    password = "super_secret_password123"
    return f"Connecting to database with {username}:{password}"


def shell_injection(user_input):
    """
    This function is vulnerable to shell injection.
    """
    # Security risk: Shell injection
    result = subprocess.call(f"echo {user_input}", shell=True)
    return result

# Styling issue: Inconsistent indentation and line length
if __name__ == "__main__":
   print("Running bug-infested code...")
   result = insecure_file_handling("sensitive_data.txt")
   print(performance_hog(1000))
   obj = PoorlyDocumentedClass(5)
   print(obj.poorly_named_method())
   print(obj.potential_division_by_zero(0))
   print(unused_import_and_variable())
   print(global_variable_abuse())
   resource_leak()
   print(infinite_recursion(10))  # This will cause a runtime error
   hardocoded_password()
   shell_injection("ls")
   # calling undefined function
   undef()
   print("This line will never be reached due to the error above")
