import re
from itertools import groupby

from bs4 import BeautifulSoup

from api.jpred import submit_jpred


def generate(sequence):
    result = submit_jpred(sequence)
    print(f"STATUS CODE: {result.status_code}")
    link = result.headers['Location']
    jobid = re.search(r"(jp_.*)$", link).group(1)
    simple = f"http://www.compbio.dundee.ac.uk/jpred4/results/{jobid}/{jobid}.simple.html"
    # return jsonify(job_id=jobid, simple_url=simple)
    return simple


def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    code = str(soup.code)
    code = code.strip("\n</code>")
    structures = code.split("\n")
    primary_structure = structures[0]
    secondary_structure = structures[1]
    secondary_structure = re.sub('<[^>]+>', '', secondary_structure)
    return primary_structure, secondary_structure


def structure_to_list(secondary_structure):
    groups = groupby(secondary_structure)
    grouped_chars = [(label, sum(1 for _ in group)) for label, group in groups]
    print(grouped_chars)

    secondary_list = []
    count = 0
    for group in grouped_chars:

        if group[0] == 'H':
            secondary_list.append({"category": "secondary structure",
                                   "type": "helix",
                                   "start": count,
                                   "end": count + group[1]})
        elif group[0] == 'E':
            secondary_list.append({"category": "secondary structure",
                                   "type": "beta_strand",
                                   "start": count,
                                   "end": count + group[1]})
        count += group[1]
    return secondary_list
