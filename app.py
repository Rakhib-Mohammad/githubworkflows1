from flask import Flask

app=Flask(__name__)

## A simple route that returns "Hello World!"

@app.route("/")
def home():
    return "Hello World! App is running."

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)