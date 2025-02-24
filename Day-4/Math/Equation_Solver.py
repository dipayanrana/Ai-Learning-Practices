# Solves equations of the form ax+b=c.

def solve_equation(a, b, c):  
    try:  
        x = (c - b) / a  
        return f"x = {x}"  
    except ZeroDivisionError:  
        return "Error: 'a' cannot be zero!"  

print(solve_equation(2, 5, 15))  # Output: x = 5.0  
print(solve_equation(0, 3, 5))    # Output: Error!  