from flask import Flask, jsonify  
import numpy as np  

app = Flask(__name__)  

@app.route('/')  
def home():  
    return "Vector & Matrix Calculator"  

# Vector Addition Endpoint  
@app.route('/vector/add/<vector1>/<vector2>')  
def add_vectors(vector1, vector2):  
    try:  
        v1 = np.array(eval(vector1))  # Convert string input to array  
        v2 = np.array(eval(vector2))  
        result = (v1 + v2).tolist()   # Convert NumPy array to list for JSON  
        return jsonify({"result": result})  
    except Exception as e:  
        return jsonify({"error": str(e)})  

# Matrix Multiplication Endpoint  
@app.route('/matrix/multiply/<matrix1>/<matrix2>')  
def multiply_matrices(matrix1, matrix2):  
    try:  
        m1 = np.array(eval(matrix1))  
        m2 = np.array(eval(matrix2))  
        result = np.dot(m1, m2).tolist()  
        return jsonify({"result": result})  
    except Exception as e:  
        return jsonify({"error": str(e)})  

if __name__ == '__main__':  
    app.run(debug=True)  