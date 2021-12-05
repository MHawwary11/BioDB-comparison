# Group 02 

#  Cross Verification of Protein Information

Package to see how two sets of human proteins from UniProt and RefSeq match up.

## Installation 
To install the package, navigate to `./group02,` then use the following command:

`pip install project_package/`

## Usage 

The package contains the files responsible for Downloading, mapping and comparing data acquired from the two databases.

You can use the package using any of the following ways:


- `import DBVC` to import all the files<br />
- `import DBVC.filename` to import a specific file from the package<br />
- `from DBVC.filename import methodname` to import a specific method from a file in the package 


# BEFORE YOU START
1. The commands in the next two sections (download and map) **MUST** be executed first before you can search for a protein by name/accession identifier.
1. If you pull everything from the repository including the files in the 'data' folder, then you won't have to re-execute these commands and the files will be ready for use, so you can skip the 'download' and 'map' sections.
1. It takes approximately an hour to download the data from RefSeq.
1. It takes approximately 8 mins. to download the data from UniProt.

### Download data from databases RefSeq and UniProt
```bash
cd ./group02/project_package
python cli.py download-refseq --output-path ./data/refseq.tsv
python cli.py download-uniprot --output-path ./data/uniprot.tsv
```
### Map Metadata from UniProt and RefSeq
```bash
cd ./group02/project_package
python cli.py map-data ./data/uniprot.tsv ./data/refseq.tsv ./data/new_out.tsv
```

### Calculate Summary Statistics of Human Proteome
```bash
cd ./group02/project_package
python cli.py analyse-protein-metadata ./data/new_out.tsv
```

### Retrieve Metadata of a Protein
```bash
cd ./group02/project_package
python cli.py analyse-protein-metadata ./data/new_out.tsv -p P10275 
python cli.py analyse-protein-metadata ./data/new_out.tsv -p AR 
python cli.py analyse-protein-metadata ./data/new_out.tsv --protein NP_001334993
python cli.py analyse-protein-metadata ./data/new_out.tsv --protein DHTR
```
