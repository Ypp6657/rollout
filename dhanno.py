from flask import Flask

app = Flask(__name__)

@app.route('/')

def dhanno():
    return "Sansar bai avghad toh pakka Dhananjay rao n ch naav ghet Navra Mazha Chakka"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
