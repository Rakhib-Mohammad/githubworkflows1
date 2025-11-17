from flask import Flask

app=Flask(__name__)

## A simple route that returns "Hello World!"
### Return "Hello World! App is running."

@app.route("/")
def home():
    return "Hello World!"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)