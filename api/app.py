from flask import Flask

app = Flask(__name__, static_folder="../app/pssp/build", static_url_path="/")

app.config["DEBUG"] = True
app.config["TESTING"] = True

from routes import *


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)