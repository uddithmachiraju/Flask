from flask import Flask 

app = Flask(__name__)

@app.route("/square/<int:number>")
def square(number):
    return f"Square of {number}: {number * number}"

if __name__ == "__main__":
    app.run(port = 5000, debug = True) 