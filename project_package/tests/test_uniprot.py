import os
from unittest import TestCase

from DBCV.uniprot import download_uniprot, generate_payload


class Test(TestCase):
    """
    Class to test the data downloaded from Uniprot API.
    """

    def test_payload(self):
        """
        Test downloaded payload.
        :return:
        """
        d = {
            'columns': 'genes,id,database(HGNC),database(RefSeq),sequence',
            'format': 'tab',
            'query': 'organism :"Homo sapiens (Human) [9606]" AND proteome:up000005640'
        }
        self.assertEqual(generate_payload(), d)

    def test_download_uniprot(self):
        """
        Test that the file is being downloaded.
        :return:
        """
        path = 'my_test.txt'

        payload = {
            'query': 'organism :"Homo sapiens (Human) [9606]" AND O95825',
            'format': 'tab',
            'columns': ','.join(['genes', 'id', 'database(HGNC)', 'database(RefSeq)', 'sequence']),
        }

        download_uniprot(payload, path)
        self.assertTrue(os.path.exists(path))
        os.remove(path)
