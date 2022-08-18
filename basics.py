from tempfile import template
from flask import Flask, render_template


@app.route('/home')
def home():
    return render_template("home.html")


app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)
