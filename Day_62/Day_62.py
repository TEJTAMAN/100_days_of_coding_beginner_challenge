#Create a simple web server using Flask or Django.


#pip install flask


from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is a simple Flask web server."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
