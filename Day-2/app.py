from flask import Flask  
app = Flask(__name__)  

@app.route('/')  
def hello():  
    return "Hello, AI Engineer!"  

@app.route('/equation')  
def equation():  
    return "3x + 2y = 16"  

if __name__ == '__main__':  
    app.run()  