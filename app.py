from flask import Flask
from flask import render_template, jsonify

from stock_scraper import get_data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data", methods=['GET'])
def data():
    get_data()
    # return jsonify(get_data())
    return "LOL"


if __name__ == "__main__":
    app.run(debug=True)
