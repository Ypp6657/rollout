from flask import Flask

app = Flask(__name__)

@app.route('/')

def dhanno():
    return "Welcome to KUBERNETES!!!!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=7000, debug=True)
