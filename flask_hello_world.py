#Author : Roche Christopher
#File created on 24 Oct 2019 8:13 AM

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Failure is not option"

@app.route('/apollo')
def apollo():
    return "tranquility base here.. The Eagle has landed"

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)

