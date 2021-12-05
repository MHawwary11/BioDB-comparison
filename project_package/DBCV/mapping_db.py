import pandas as pd
import os

"""
using pandas datafram to read uniprot & refseq_final in tabular form 
"""

def map_db(uniprot_path, refseq_path, out_path):
    
    # Dataframe for the uniprot file
    uniprot_df = pd.read_csv(uniprot_path, sep='\t', header=0)

    # Dataframe for the refseq file
    refseq_df = pd.read_csv(refseq_path, sep='\t', header=0)

    # Changing the column names for Uniprot dataframe
    uniprot_df.columns = ['Gene_Names_Uniprot', 'Entry_Uniprot','HGNC_Uniprot','accession_number_version','Sequence_Uniprot']

    # Changing the column names for RefSeq dataframe
    refseq_df.columns = ['Refseq_accession_number_Refseq', 'accession_number_version','db_source_accession_Refseq','Sequence_Refseq','Entry_Uniprot_Refseq','Gene_Name_Refseq',
                 'Gene_synonyms_Refseq','Gene_ID_Refseq','HGNC_Refseq','MimID_Refseq']
    
    # Modified uniprot file
    modified_uniprot = 'new_uniprot.tsv'
    
    # Creating a modified uniprot file as output
    with open(modified_uniprot,"w") as f:

        # Writing the file header
        f.write("Entry_Uniprot" + "\t" + "accession_number_version" + "\t" + "HGNC_Uniprot"
                + "\t" + "Gene_Names_Uniprot" + "\t" + "Sequence_Uniprot")
        f.write("\n")

        # Iterating over the Uniprot datafile
        for index, row in uniprot_df.iterrows():

            # Converting the values in the RefSeq column to string
            k=str(row['accession_number_version'])

            # Splitting the column values into its respective RefSeq Accession Number
            k = k.split(";")
            k=k[:-1]

            # Excluding the values within the square bracket
            for i in k:
                i=i.split("[")[0]
                i = i.strip()

                # Writing the entries to the modified file with all the relevant columns
                f.write(str(row['Entry_Uniprot'])+ "\t" + i + "\t" + str(row['HGNC_Uniprot']) + "\t" + str(row['Gene_Names_Uniprot']) + "\t" + str(row['Sequence_Uniprot']))

                f.write('\n')


    # Dataframe for the modified  Uniprot file
    df3_newuniprot = pd.read_csv(modified_uniprot, sep='\t', header=0)

    # Merging the modified Uniprot dataframe and the RefSeq dataframes based on the  ReSeq accession number 

    df4_mergefiles = pd.merge(refseq_df, df3_newuniprot, on='accession_number_version')

    # Rearraging the columns of the dataframe for better interpretation

    df4_mergefiles = df4_mergefiles[['accession_number_version','Refseq_accession_number_Refseq','db_source_accession_Refseq','Entry_Uniprot','Entry_Uniprot_Refseq',
              'HGNC_Uniprot','HGNC_Refseq','MimID_Refseq','Gene_Names_Uniprot','Gene_Name_Refseq','Gene_synonyms_Refseq',
              'Gene_ID_Refseq','Sequence_Uniprot','Sequence_Refseq']]

    # Writing the dataframe to an output file
    df4_mergefiles.to_csv (out_path, sep='\t',index=False, header=True)
    
    # Delete meta files from user's computer
    os.remove(modified_uniprot)
    
if __name__ == '__main__':
    
    map_db('../data/uniprot.tsv' , '../data/refseq.tsv','../data/new_out.tsv')

