from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/bar")
def bar():
    return "bar!"

if __name__ == "__main__":
    app.run()