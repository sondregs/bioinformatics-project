import re
from time import sleep
import requests
from flask import request, jsonify
from app import app
from jpred import submit_jpred
from utils import generate, parse_html, structure_to_list


api_root = ""
if app.config["TESTING"]:
    api_root = "/api"

@app.route(api_root + '/', methods=['GET'])
def index():
    return "Bioinformatics project api."


@app.route(api_root + '/test', methods=['GET'])
def test():
    result = submit_jpred("MQVWPIEGIKKFETLSYLPP")
    print(f"STATUS CODE: {result.status_code}")

    url = result.content
    link = result.headers['Location']
    jobid = re.search(r"(jp_.*)$", link).group(1)
    simple = f"http://www.compbio.dundee.ac.uk/jpred4/results/{jobid}/{jobid}.simple.html"
    return f"link: {link} , jobid: {jobid} , simple = {simple} , content: {url}"


@app.route(api_root + '/submit')
def submit():
    sequence = request.args.get("sequence", "MQVWPIEGIKKFETLSYLPP")
    simple_url = generate(sequence)
    simple_result = requests.get(simple_url)
    print(f" Simple STATUS CODE: {simple_result.status_code}")
    status = simple_result.status_code
    attempt = 0
    while status == 404 and attempt <= 300:
        sleep(1)
        print(attempt)
        print(simple_url)
        print(status)
        simple_result = requests.get(simple_url)
        status = simple_result.status_code
        attempt += 1
    if status == 200:
        primary, secondary = parse_html(simple_result.content.decode("utf-8"))
        secondary_list = structure_to_list(secondary)
        return jsonify(primary_structure=primary, secondary_structure=secondary, secondary_list=secondary_list)
    return "Sequence too long or JPRED API is down, try again later."


@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    return response


