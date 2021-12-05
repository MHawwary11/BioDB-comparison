import pandas as pd
import os

from unittest import TestCase

from DBCV.mapping_db import map_db

TEST_FOLDER = os.path.dirname(__file__)
# data for the test file I generated 
UNIPROT_FILE_PATH = os.path.join(TEST_FOLDER, 'data/uniprot_test.tsv') 
REFSEQ_FILE_PATH = os.path.join(TEST_FOLDER, 'data/refseq_test.tsv')
MERGED_FILE_PATH = os.path.join(TEST_FOLDER, 'data/new_out.tsv')


class TestMappingDb(TestCase):
    """Unit tests for the mapping module."""
    
    def test_map_db(self):
        '''
    it check wether the file is correctly generated from the two downloaded file 'uniprot & refseq' 
    '''
        map_db(UNIPROT_FILE_PATH, REFSEQ_FILE_PATH, MERGED_FILE_PATH) 
        
        # make sure if the file path is generated  
        assert os.path.exists(MERGED_FILE_PATH) == 1 
        df = pd.read_csv(MERGED_FILE_PATH, sep='\t')
        output = df[df['accession_number_version']=='NP_665857.2'].iloc[0]
        
        # check if the files are merged correctly according to choosed column 
        assert(output['Gene_Names_Uniprot'] == 'CRYZL1 4P11') 
        assert(output['Sequence_Uniprot'] == 'MKGLYFQQSSTDEEITFVFQEKEDLPVTEDNFVKLQVKACALSQINTKLLAEMKMKKDLFPVGREIAGIVLDVGSKVSFFQPDDEVVGILPLDSEDPGLCEVVRVHEHYLVHKPEKVTWTEAAGSIRDGVRAYTALHYLSHLSPGKSVLIMDGASAFGTIAIQLAHHRGAKVISTACSLEDKQCLERFRPPIARVIDVSNGKVHVAESCLEETGGLGVDIVLDAGVRLYSKDDEPAVKLQLLPHKHDIITLLGVGGHWVTTEENLQLDPPDSHCLFLKGATLAFLNDEVWNLSNVQQGKYLCILKDVMEKLSTGVFRPQLDEPIPLYEAKVSMEAVQKNQGRKKQVVQF')
        assert(output['Sequence_Refseq'] == 'MKGLYFQQSSTDEEITFVFQEKEDLPVTEDNFVKLQVKACALSQINTKLLAEMKMKKDLFPVGREIAGIVLDVGSKVSFFQPDDEVVGILPLDSEDPGLCEVVRVHEHYLVHKPEKVTWTEAAGSIRDGVRAYTALHYLSHLSPGKSVLIMDGASAFGTIAIQLAHHRGAKVISTACSLEDKQCLERFRPPIARVIDVSNGKVHVAESCLEETGGLGVDIVLDAGVRLYSKDDEPAVKLQLLPHKHDIITLLGVGGHWVTTEENLQLDPPDSHCLFLKGATLAFLNDEVWNLSNVQQGKYLCILKDVMEKLSTGVFRPQLDEPIPLYEAKVSMEAVQKNQGRKKQVVQF')
    