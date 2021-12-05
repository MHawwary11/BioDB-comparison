"""analysis module tests."""

import os
from DBCV import analysis


TEST_FOLDER = os.path.dirname(__file__)
MERGED_FILE_PATH = os.path.join(TEST_FOLDER, "data/merged_data_toy.tsv")

class TestAnalysis:
    """Unit tests for the analysis module."""

    def test_compare_data(self):
        """Checks whether the analysis module correctly generates the metadata for a given protein and calculates
        the summary statistics of all human proteins."""

        # check if protein metadata is correct
        protein = ['P10275', 'NP_001334993', 'AR', 'DHTR', 'AR8']
        for identifier in protein:
            protein_info = analysis.compare_data(filename=MERGED_FILE_PATH, protein=identifier)
            assert protein_info.iloc[0, 1] == 'AR'
            assert protein_info.iloc[0, 2] == 'AR'
            assert protein_info.iloc[0, 3] == True

            assert protein_info.iloc[1, 1] == 'P10275'
            assert protein_info.iloc[1, 2] == 'P10275'
            assert protein_info.iloc[1, 3] == True

            assert protein_info.iloc[2, 1] == 'NP_001334993.1'
            assert protein_info.iloc[2, 2] == 'NP_001334993'
            assert protein_info.iloc[2, 3] == True

            assert protein_info.iloc[3, 1] == 920
            assert protein_info.iloc[3, 2] == 572
            assert protein_info.iloc[3, 3] == False

            assert protein_info.iloc[4, 1] == 'MEVQLGLGRVYPRPPSKTYRGAFQNLFQSVREVIQNPGPRHPEAASAAPPGASLLLLQQQQQQQQQQQQQ' \
                                              'QQQQQQQQQQETSPRQQQQQQGEDGSPQAHRRGPTGYLVLDEEQQPSQPQSALECHPERGCVPEPGAAVA' \
                                              'ASKGLPQQLPAPPDEDDSAAPSTLSLLGPTFPGLSSCSADLKDILSEASTMQLLQQQQQEAVSEGSSSGR' \
                                              'AREASGAPTSSKDNYLGGTSTISDNAKELCKAVSVSMGLGVEALEHLSPGEQLRGDCMYAPLLGVPPAVR' \
                                              'PTPCAPLAECKGSLLDDSAGKSTEDTAEYSPFKGGYTKGLEGESLGCSGSAAAGSSGTLELPSTLSLYKS' \
                                              'GALDEAAAYQSRDYYNFPLALAGPPPPPPPPHPHARIKLENPLDYGSAWAAAAAQCRYGDLASLHGAGAA' \
                                              'GPGSGSPSAAASSSWHTLFTAEEGQLYGPCGGGGGGGGGGGGGGGGGGGGGGGEAGAVAPYGYTRPPQGL' \
                                              'AGQESDFTAPDVWYPGGMVSRVPYPSPTCVKSEMGPWMDSYSGPYGDMRLETARDHVLPIDYYFPPQKTC' \
                                              'LICGDEASGCHYGALTCGSCKVFFKRAAEGKQKYLCASRNDCTIDKFRRKNCPSCRLRKCYEAGMTLGAR' \
                                              'KLKKLGNLKLQEEGEASSTTSPTEETTQKLTVSHIEGYECQPIFLNVLEAIEPGVVCAGHDNNQPDSFAA' \
                                              'LLSSLNELGERQLVHVVKWAKALPGFRNLHVDDQMAVIQYSWMGLMVFAMGWRSFTNVNSRMLYFAPDLV' \
                                              'FNEYRMHKSRMYSQCVRMRHLSQEFGWLQITPQEFLCMKALLLFSIIPVDGLKNQKFFDELRMNYIKELD' \
                                              'RIIACKRKNPTSCSRRFYQLTKLLDSVQPIARELHQFTFDLLIKSHMVSVDFPEMMAEIISVQVPKILSG' \
                                              'KVKPIYFHTQ'
            assert protein_info.iloc[4, 2] == 'MEVQLGLGRVYPRPPSKTYRGAFQNLFQSVREVIQNPGPRHPEAASAAPPGASLLLLQQQQQQQQQQQQQ' \
                                              'QQQQQQQQQQETSPRQQQQQQGEDGSPQAHRRGPTGYLVLDEEQQPSQPQSALECHPERGCVPEPGAAVA' \
                                              'ASKGLPQQLPAPPDEDDSAAPSTLSLLGPTFPGLSSCSADLKDILSEASTMQLLQQQQQEAVSEGSSSGR' \
                                              'AREASGAPTSSKDNYLGGTSTISDNAKELCKAVSVSMGLGVEALEHLSPGEQLRGDCMYAPLLGVPPAVR' \
                                              'PTPCAPLAECKGSLLDDSAGKSTEDTAEYSPFKGGYTKGLEGESLGCSGSAAAGSSGTLELPSTLSLYKS' \
                                              'GALDEAAAYQSRDYYNFPLALAGPPPPPPPPHPHARIKLENPLDYGSAWAAAAAQCRYGDLASLHGAGAA' \
                                              'GPGSGSPSAAASSSWHTLFTAEEGQLYGPCGGGGGGGGGGGGGGGGGGGGGGGEAGAVAPYGYTRPPQGL' \
                                              'AGQESDFTAPDVWYPGGMVSRVPYPSPTCVKSEMGPWMDSYSGPYGDMRNTRRKRLWKLIIRSINSCICS' \
                                              'PRETEVPVRQQK'
            assert protein_info.iloc[4, 3] == False

        # check if summary statistics of all human proteins are correct
        summary_statistics = analysis.compare_data(filename=MERGED_FILE_PATH)
        assert summary_statistics.iloc[0, 1] == 100.0
        assert summary_statistics.iloc[1, 1] == 39.0
        assert summary_statistics.iloc[2, 1] == 100.0
        assert summary_statistics.iloc[3, 1] == 34.0
        assert summary_statistics.iloc[4, 1] == 33.0
