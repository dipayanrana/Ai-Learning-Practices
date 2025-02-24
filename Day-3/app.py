from flask import Flask
app = Flask(__name__)

def solve_system(a1, b1, c1, a2, b2, c2):  
    try:  
        x = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)  
        y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)  
        return f"x = {x}, y = {y}"  
    except ZeroDivisionError:  
        return "No unique solution!"

@app.route('/')
def home():
    return "Welcome to the Equation Solver!"

@app.route('/solve-system')
def solve():
    # Use example values or retrieve parameters from the request
    result = solve_system(2, 1, 10, 1, -1, 2)
    return f"Equation Solver Result: {result}"

if __name__ == '__main__':
    app.run(debug=True)

