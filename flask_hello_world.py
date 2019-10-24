#Author : Roche Christopher
#File created on 24 Oct 2019 8:13 AM

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Failure is not option"

@app.route('/apollo')
def apollo():
    return "tranquility base here.. The Eagle has landed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 6060)

