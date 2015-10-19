from flask import Flask
from flask import render_template, jsonify

from stock_scraper import get_stock_data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data", methods=['GET'])
def data():
    stock_data = get_stock_data()
    print "STOCK DATA:", stock_data
    # return jsonify(get_data())
    # return "FUCK YOU"
    return jsonify(data=stock_data)


if __name__ == "__main__":
    app.run(debug=True)
