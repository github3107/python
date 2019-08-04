from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Mr. Ramesh Pendem!"

if __name__ == "__main__":
    app.run()
