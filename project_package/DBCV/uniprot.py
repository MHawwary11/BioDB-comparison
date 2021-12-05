import os

import requests

BASE = 'http://www.uniprot.org'
KB_ENDPOINT = '/uniprot/'
TOOL_ENDPOINT = '/uploadlists/'


def generate_payload():
    """
    Payload for the API query "https://www.uniprot.org/uniprot/?query=proteome:UP000005640"
    Documentation can be found here:
    https://bioservices.readthedocs.io/en/master/_modules/bioservices/uniprot.html
    :return: payload for the API query
    """
    return {
        'query': 'organism :"Homo sapiens (Human) [9606]" AND proteome:up000005640',
        'format': 'tab',
        'columns': ','.join(['genes', 'id', 'database(HGNC)', 'database(RefSeq)', 'sequence']),
    }


def download_uniprot(payload: dict, output_path: str = "../data/uniprot.tsv"):
    """
    Download information from UniProt based on the payload.
    :param payload: payload for API query
    :param output_path: path for the output file
    :return:
    """

    if os.path.exists(output_path):
        print(f"File {output_path} already exists")
        return
    result = requests.get(BASE + KB_ENDPOINT, params=payload)
    if result.ok:
        with open(output_path, 'a') as f:
            f.write(result.text)
    else:
        print(result.status_code)


if __name__ == '__main__':
    download_uniprot(generate_payload())
