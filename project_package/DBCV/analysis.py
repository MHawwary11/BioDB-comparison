import pandas as pd
from pandas import DataFrame


def compare_data(filename: str, protein: str = None) -> DataFrame:
    """Compares protein(s) metadata between UniProt and NCBI RefSeq databases
    :param filename: tsv file path containing merged data from both databases
    :param protein: UniProt accession identifier, RefSeq accession identifier, or gene symbol
    :return: a dataframe comparing the metadata of a single given protein between the two databases or
    a dataframe of the summary statistics of all human proteins
    """
    df = pd.read_csv(filename, sep='\t')

    # compare metadata of a given protein
    if protein:
        for row in range(len(df)):
            # check if the  given protein UniProt accession identifier, RefSeq accession identifier, or gene symbol
            # present in the respective columns including the other UniProt gene names and RefSeq gene name synonyms
            if protein in df.iloc[row, :].values or protein in str(
                    df.iloc[row, df.columns.get_loc('Gene_Names_Uniprot')]).split(' ') or protein in df.iloc[row, df.columns.get_loc('Gene_synonyms_Refseq')].split('; '):



                # generate dataframe with each entry fro each database and whether both databases match or not
                protein_info_columns = ['Metadata Category', 'UniProt', 'NCBI RefSeq', 'Match']

                # Protein's gene symbol --> first UniProt gene name VS RefSeq gene name
                # UniProt accession IDs --> UniProt Entry ID VS UniProt Entry ID in RefSeq
                # RefSeq accession IDs --> accessio number version without version number VS RefSeq accession number
                # Amino Acid sequences lengths --> amino acid sequence length in UniProt VS amino acid sequence length
                # in RefSeq
                # Amino Acid sequences alignments --> amino acid sequence in UniProt VS amino acid sequence in RefSeq
                protein_info_data = [
                    ["Protein's gene symbol", str(df.iloc[row, df.columns.get_loc('Gene_Names_Uniprot')]).split(' ')[0],
                     df.iloc[row, df.columns.get_loc('Gene_Name_Refseq')],
                     str(df.iloc[row, df.columns.get_loc('Gene_Names_Uniprot')]).split(' ')[0] == df.iloc[
                         row, df.columns.get_loc('Gene_Name_Refseq')]],
                    ["UniProt accession IDs", df.iloc[row, df.columns.get_loc('Entry_Uniprot')],
                     df.iloc[row, df.columns.get_loc('Entry_Uniprot_Refseq')],
                     df.iloc[row, df.columns.get_loc('Entry_Uniprot')] == df.iloc[
                         row, df.columns.get_loc('Entry_Uniprot_Refseq')]],
                    ["RefSeq accession IDs", df.iloc[row, df.columns.get_loc('accession_number_version')],
                     df.iloc[row, df.columns.get_loc('Refseq_accession_number_Refseq')],
                     df.iloc[row, df.columns.get_loc('accession_number_version')].split('.')[0] == df.iloc[
                         row, df.columns.get_loc('Refseq_accession_number_Refseq')]],
                    ["Amino Acid sequences lengths", len(df.iloc[row, df.columns.get_loc('Sequence_Uniprot')]),
                     len(df.iloc[row, df.columns.get_loc('Sequence_Refseq')]),
                     len(df.iloc[row, df.columns.get_loc('Sequence_Uniprot')]) == len(
                         df.iloc[row, df.columns.get_loc('Sequence_Refseq')])],
                    ["Amino Acid sequences alignments", df.iloc[row, df.columns.get_loc('Sequence_Uniprot')],
                     df.iloc[row, df.columns.get_loc('Sequence_Refseq')],
                     df.iloc[row, df.columns.get_loc('Sequence_Uniprot')] == df.iloc[
                         row, df.columns.get_loc('Sequence_Refseq')]]
                ]
                protein_info = pd.DataFrame(data=protein_info_data, columns=protein_info_columns)

                return protein_info

    else:  # compare metadata for the all human proteins between the two databases
        total = len(df)  # number of human proteins
        matching_gene_symbols = 0  # number of matching Protein's gene symbol in both databases
        matching_uniprot_accession_ids = 0  # number of matching UniProt accession IDs in both databases
        matching_refseq_accession_ids = 0  # number of matching RefSeq accession IDs in both databases
        matching_aa_lengths = 0  # number of matching Amino Acid sequences lengths in both databases
        matching_aa_sequences = 0  # number of matching Amino Acid sequences alignments in both databases

        # same comparison as previously done with a single protein, but this time with keeping the count
        for row in range(len(df)):
            if str(df.iloc[row, df.columns.get_loc('Gene_Names_Uniprot')]).split(' ')[0] == df.iloc[row, df.columns.get_loc('Gene_Name_Refseq')]:
                matching_gene_symbols += 1

            if df.iloc[row, df.columns.get_loc('Entry_Uniprot')] == df.iloc[
                row, df.columns.get_loc('Entry_Uniprot_Refseq')]:
                matching_uniprot_accession_ids += 1

            if df.iloc[row, df.columns.get_loc('accession_number_version')].split('.')[0] == df.iloc[
                row, df.columns.get_loc('Refseq_accession_number_Refseq')]:
                matching_refseq_accession_ids += 1

            if len(df.iloc[row, df.columns.get_loc('Sequence_Uniprot')]) == len(
                    df.iloc[row, df.columns.get_loc('Sequence_Refseq')]):
                matching_aa_lengths += 1

            if df.iloc[row, df.columns.get_loc('Sequence_Uniprot')] == df.iloc[
                row, df.columns.get_loc('Sequence_Refseq')]:
                matching_aa_sequences += 1

        # generate a dataframe with the percentage of how much each metadata caregory matches between the two databases
        summary_statistics_columns = ['UniProt vs NCBI RefSeq', 'Matching Percentage']
        summary_statistics_data = [
            ["Protein's gene symbol", round((matching_gene_symbols / total) * 100, 2)],
            ["UniProt accession IDs", round((matching_uniprot_accession_ids / total) * 100, 2)],
            ["RefSeq accession IDs", round((matching_refseq_accession_ids / total) * 100, 2)],
            ["Amino Acid sequences lengths", round((matching_aa_lengths / total) * 100, 2)],
            ["Amino Acid sequences alignments", round((matching_aa_sequences / total) * 100, 2)]
        ]
        summary_statistics = pd.DataFrame(data=summary_statistics_data, columns=summary_statistics_columns)

        return summary_statistics