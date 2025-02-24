def solve_system(a1, b1, c1, a2, b2, c2):  
    try:  
        # Solve using elimination  
        x = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)  
        y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)  
        return f"x = {x}, y = {y}"  
    except ZeroDivisionError:  
        return "No unique solution!"  

