from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        {
            "Message" : "Hii world"
        }
    )

@app.route("/greet", methods = ['POST'])
def greet():
    data = request.get_json()

    if 'name' not in data:
        return jsonify(
            {
                "Message" : "Name not in Data" 
            }
        )
    
    name = data['name']
    
    return jsonify(
        {
            "Message" : f"Hii {name}" 
        }
    )

if __name__ == "__main__":
    app.run(debug = True, port = 5000) 