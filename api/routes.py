from api.app import app


@app.route('/', methods=['GET'])
def index():
    return "Bioinformatics project api."


@app.route('/api/asdf', methods=['GET'])
def get_asdf():
    return "asdf"
