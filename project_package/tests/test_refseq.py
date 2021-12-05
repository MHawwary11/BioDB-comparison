import os
from unittest import TestCase

from Bio.GenBank.Record import Qualifier, Feature, Record

from DBCV.refseq import augment_data, download_refseq


class TestRefseq(TestCase):
    """
    Class to test downloading of RefSeq data.
    """

    def test_augment_data(self):
        """
        Test of the data that was extracted from the API.
        :return:
        """
        gold = {
            'accession': 'ACCESSION_1',
            'accession_version': 'v1',
            'db_source_accession': 'DB_ACCESSION_SOURCE_1',
            'sequence': 'SEQUENCE',
            'uniprot_accession': 'test',
            'gene_id': 'VALUE',
            'gene_synonym': 'VALUE',
        }
        self.assertEqual(augment_data(self._mock_record()), gold)

    def test_download_refseq(self):
        """
        Test that the file is being downloaded.
        :return:
        """
        path = 'my_path.txt'
        download_refseq(path, entries_number=1)
        self.assertTrue(os.path.exists(path))
        os.remove(path)

    def _mock_record(self) -> Record:
        """
        Creating mock record for testing.
        :return: mock record
        """
        mock_f1 = self._cds_feature()
        mock_f2 = self._site_feature()

        mock_r = Record()
        mock_r.accession = ['ACCESSION_1']
        mock_r.version = 'v1'
        mock_r.db_source = '1 2 DB_ACCESSION_SOURCE_1'
        mock_r.sequence = 'SEQUENCE'

        mock_r.features.append(mock_f1)
        mock_r.features.append(mock_f2)
        return mock_r

    def _site_feature(self) -> Feature:
        """
        Mock site feature.
        :return: feature object
        """
        mock_q_note = Qualifier()
        mock_q_note.key = '/note='
        mock_q_note.value = 'UniProtKB/Swiss-Prot (test)'
        mock_f2 = Feature()
        mock_f2.key = 'Site'
        mock_f2.qualifiers.append(mock_q_note)
        return mock_f2

    def _cds_feature(self) -> Feature:
        """
        Mock cds feature
        :return: feature object
        """
        mock_q_gene = Qualifier()
        mock_q_gene.key = '/gene='
        mock_q_gene.value = '"VALUE"'
        mock_q_gene_id = Qualifier()
        mock_q_gene_id.key = '/gene_synonym='
        mock_q_gene_id.value = '"VALUE"'
        mock_q_db_ref = Qualifier()
        mock_q_db_ref.key = '/db_xref='
        mock_q_db_ref.value = '"VALUE:123"'
        mock_f1 = Feature()
        mock_f1.key = 'CDS'
        mock_f1.qualifiers.append(mock_q_gene)
        mock_f1.qualifiers.append(mock_q_gene_id)
        mock_f1.qualifiers.append(mock_q_db_ref)
        return mock_f1
