from flask import Flask

app = Flask(__name__)

@app.route('/')

def dhanno():
    return "I am bored.....tomorrow I will have Old Monk and Jaggermite with some Jenkins!!!!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=7000, debug=True)
