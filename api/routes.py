import re
from time import sleep

import requests
from flask import request, jsonify
from bs4 import BeautifulSoup

from api.app import app
from api.jpred import submit_jpred, status_jpred


@app.route('/', methods=['GET'])
def index():
    return "Bioinformatics project api."


@app.route('/api/test', methods=['GET'])
def test():
    result = submit_jpred("MQVWPIEGIKKFETLSYLPP")
    print(f"STATUS CODE: {result.status_code}")

    url = result.content
    link = result.headers['Location']
    jobid = re.search(r"(jp_.*)$", link).group(1)
    simple = f"http://www.compbio.dundee.ac.uk/jpred4/results/{jobid}/{jobid}.simple.html"
    #response = requests.get(simple)
    #print(f"STATUS CODE: {response.status_code}")
    return f"link: {link} , jobid: {jobid} , simple = {simple} , content: {url}"
    #return response.content


@app.route('/api/submit')
def submit():
    sequence = request.args.get("sequence", "MQVWPIEGIKKFETLSYLPP")
    simple_url = generate(sequence)
    simple_result = requests.get(simple_url)
    print(f" Simple STATUS CODE: {simple_result.status_code}")
    status = simple_result.status_code
    attempt = 0
    while status == 404 and attempt <= 10:
        sleep(1)
        print(attempt)
        print(simple_url)
        print(status)
        simple_result = requests.get(simple_url)
        status = simple_result.status_code
        attempt += 1
    if status == 200:
        primary, secondary = parse_HTML(simple_result.content.decode("utf-8"))
        return jsonify(primary_structure=primary, secondary_structure=secondary)
    return "Sequence too long or JPRED API is down, try again later."


def generate(sequence):
    result = submit_jpred(sequence)
    print(f"STATUS CODE: {result.status_code}")
    link = result.headers['Location']
    jobid = re.search(r"(jp_.*)$", link).group(1)
    simple = f"http://www.compbio.dundee.ac.uk/jpred4/results/{jobid}/{jobid}.simple.html"
    #return jsonify(job_id=jobid, simple_url=simple)
    return simple

def parse_HTML(HTML_content):
    soup = BeautifulSoup(HTML_content, 'html.parser')
    code = str(soup.code)
    code = code.strip("\n</code>")
    structures = code.split("\n")
    primary_structure = structures[0]
    secondary_structure = structures[1]
    secondary_structure = re.sub('<[^>]+>', '', secondary_structure)
    return primary_structure, secondary_structure
