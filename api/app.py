from flask import Flask

app = Flask(__name__, static_folder="../build", static_url_path="/")

app.config["DEBUG"] = True

from api import routes


if __name__ == "__main__":
    app.run(host='0.0.0.0')