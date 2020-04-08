import re

from api.app import app
from api.jpred import submit_jpred, status_jpred
import requests
from time import sleep


@app.route('/', methods=['GET'])
def index():
    return "Bioinformatics project api."


@app.route('/api/test', methods=['GET'])
def test():
    result = submit_jpred()
    print(f"STATUS CODE: {result.status_code}")

    # url = result.content
    link = result.headers['Location']
    jobid = re.search(r"(jp_.*)$", link).group(1)
    simple = f"http://www.compbio.dundee.ac.uk/jpred4/results/{jobid}/{jobid}.simple.html"
    sleep(10)
    response = requests.get(simple)
    print(f"STATUS CODE: {response.status_code}")
    #return f"link: {link} , jobid: {jobid} , simple = {simple} , content: {url}"
    return response.content
