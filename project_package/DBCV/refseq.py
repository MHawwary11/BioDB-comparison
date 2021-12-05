import csv
import os
from typing import Dict
import re

from Bio import Entrez, GenBank
from Bio.GenBank.Record import Record, Feature, Qualifier

Entrez.email = 'A.N.Other@example.com'


def download_refseq(output_path: str, entries_number: int = 120_000):
    """
    Fetch entries form NCBI protein database using Entrez API functions.
    API query: "Homo sapiens[Orgn] AND refseq[filter]"
    GenBank parse is used for reading the fetched data.
    https://biopython.readthedocs.io/en/latest/chapter_entrez.html
    :param entries_number: number of entries
    :param output_path: path to output file
    :return:
    """
    if os.path.exists(output_path):
        print(f"File {output_path} already exists")
        return

    add_headers(output_path=output_path)
    handle = Entrez.esearch(db="protein", term="Homo sapiens[Orgn] AND refseq[filter]", retmax=entries_number)
    record = Entrez.read(handle)
    for i in range(0, entries_number, 101):

        handle = Entrez.efetch(db="protein", id=record['IdList'][i:i + 100], rettype="gp", retmode="text")
        records = GenBank.parse(handle)

        for r in records:
            data = augment_data(r)
            write_data(data, output_path)
        handle.close()


def write_data(data: Dict[str, str], output_path: str):
    """
    Write data to a csv file.
    :param data: data to write to file
    :param output_path: path to output file
    :return:
    """
    with open(output_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data.values())


def augment_data(r: Record) -> Dict[str, str]:
    """
    Extract needed information from the Record fetched from NCBI protein database.
    :param r: Record
    :return:
    """
    data = {
        'accession': r.accession[0],
        'accession_version': r.version,
        'db_source_accession': r.db_source.split(' ')[2],
        'sequence': r.sequence,
        'uniprot_accession': ''
    }
    for f in r.features:
        f: Feature
        if f.key == 'CDS':
            for q in f.qualifiers:
                q: Qualifier
                if q.key == '/gene=':
                    data['gene_id'] = q.value.replace('"', '')
                if q.key == '/gene_synonym=':
                    data['gene_synonym'] = q.value.replace('"', '')
                if q.key == '/db_xref=':
                    k, v = q.value.replace('"', '').split(':', 1)
                    if k in ['GeneID', 'HGNC', 'MIM']:
                        data[k] = v
        if f.key == 'Site':
            for q in f.qualifiers:
                q: Qualifier
                if q.key == '/note=':
                    m = re.search(r'UniProtKB\/Swiss-Prot \((.*)\)', q.value)
                    if m:
                        uniprot_accession = m.group(1).split('.')[0]
                        data['uniprot_accession'] = uniprot_accession

    return data


def add_headers(output_path: str):
    """
    Add headers to a csv file
    :param output_path: output path of the file
    :return:
    """
    header = [
        'refseq_accession_number',
        'accession_number_version',
        'db_source_accession',
        'sequence',
        'uniprot_accession',
        'gene_name',
        'gene_synonyms',
        'gene_id',
        'HGNC',
        'mim_id'
    ]
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)


if __name__ == '__main__':
    download_refseq('../data/refseq.tsv')
