from flask import Flask
from flask import jsonify
from flask import request
import requests

app = Flask(__name__)


@app.route("/", methods=['POST'])
def scrape():
    data = request.get_json()
    url = data['url']
    # Send a POST request to the Service to invoke the Kubeless function
    r = requests.post("http://scraper:8080", json={"url": url})
    return r.text


if __name__ == "__main__":
    app.run(host='0.0.0.0')
