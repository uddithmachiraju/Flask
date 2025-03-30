from flask import Flask, jsonify 

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        {
           "Message" : "Hii this a Flask API"
        }
    )

@app.route("/info")
def info():
    return jsonify(
        {
            "app" : "Flask API",
            "version" : "1.0"
        }
    )

if __name__ == "__main__":
    app.run(port = 5000, debug = True) 