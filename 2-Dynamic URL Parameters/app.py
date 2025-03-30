from flask import Flask

app = Flask(__name__)

@app.route("/home/<username>") 
def main(username):
    return f"Hello {username}" 

if __name__ == "__main__":
    app.run(port = 5000, debug = True) 