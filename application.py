from flask import Flask, render_template, jsonify, request, abort
import config

from yelp import get_businesses

application = Flask(__name__)

# Renders UI
@application.route("/")
def home():
    return render_template("homepage.html", city=request.args.get("city", ""))


# API Endpoints
@application.route("/api/places/<city>") 
def places(city):
    businesses = get_businesses(city) 
    return jsonify(businesses)

if __name__ == "__main__":
    application.run()
