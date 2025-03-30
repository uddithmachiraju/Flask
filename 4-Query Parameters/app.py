from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/sum")
def sum_numbers():
    arg_a = request.args.get("a", type = int)
    arg_b = request.args.get("b", type = int)

    if arg_a is None or arg_b is None:
        return jsonify(
            {
                "message" : "Both a and b parameters are required"
            }
        )
    
    return jsonify(
        {
            "sum" : arg_a + arg_b
        }
    )

if __name__ == "__main__":
    app.run(port = 5000, debug = True) 