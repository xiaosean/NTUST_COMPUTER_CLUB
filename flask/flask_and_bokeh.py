from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
# use http://127.0.0.1:5000/donut/
@app.route("/donut/")
def donut():
    return app.send_static_file('NTUST_eng_donut.html')
if __name__ == "__main__":
    app.run(debug=True)
