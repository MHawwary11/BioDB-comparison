import click

from DBCV.refseq import download_refseq
from DBCV.uniprot import download_uniprot, generate_payload
from DBCV import mapping_db
from DBCV import analysis


@click.group()
def download():
    pass

@click.group()
def mapping():
    """Merge data between uniprot and refseq files."""
    pass

@click.group()
def analyse():
    """Entry method."""
    pass


@click.option('--output-path',
              required=True,
              help='path to an output tsv file. Default path is "../data/uniprot.tsv"')
@download.command(name='download-uniprot')
def download_uniprot_data(output_path):
    """
    Download information on proteins belonging to Homo sapiens from UniProt
    based on the query: "Homo sapiens (Human) [9606]" AND proteome:up000005640'
    Example:
    python cli.py download-uniprot --output-path ./data/uniprot.tsv

    :param output_path: path to output file. Default path "../data/uniprot.tsv"
    :return:
    """
    click.echo('Downloading uniprot...')
    click.echo(output_path)
    download_uniprot(generate_payload(), output_path)


@click.option('--output-path',
              required=True,
              help='path to an output tsv file. Default path is "../data/refseq.tsv"')
@download.command(name='download-refseq')
def download_refseq_data(output_path):
    """
    Download information on proterins from RefSeq database.
    API query for esearch Entrez "Homo sapiens[Orgn] AND refseq[filter]"
    Example:
    python cli.py download-refseq --output-path ./data/refseq.tsv

    :param output_path: path to output file. Default path "./data/refseq.tsv"
    :return:
    """
    click.echo('Downloading refseq...')
    download_refseq(output_path)


@mapping.command(help="Merge data between uniprot and refseq files", name="map-data")
@click.argument('uniprot_path', type=click.Path(exists=True))
@click.argument('refseq_path', type=click.Path(exists=True))
@click.argument('out_path', type=click.Path())
def map_data(uniprot_path: click.Path(), refseq_path: click.Path(), out_path: click.Path()) -> None:
    """Map data between uniprot and refseq files
    Args:
        uniprot_path (File): The uniprot file.
        refseq_path (File): The refseq file.
        out_path (File): The output path.
    """
    click.echo(mapping_db.map_db(uniprot_path=uniprot_path, refseq_path=refseq_path, out_path=out_path))


@analyse.command(name='analyse-protein-metadata')
@click.argument('merged_databases')
@click.option('-p', '--protein', default=None, help="UniProt accession identifier, RefSeq accession identifier, or gene "
                                                    "symbol")
def analyse_metadata(merged_databases: str, protein: str) -> None:
    """Prints dataframe of the summary statistics for all human proteins or the metadata of the given protein.
    :param merged_databases: tsv file path containing merged data from both databases
    :param protein: UniProt accession identifier, RefSeq accession identifier, or gene symbol
    """
    click.echo(analysis.compare_data(filename=merged_databases, protein=protein))

cli = click.CommandCollection(
    sources=[
        download,
        mapping,
        analyse
    ]
)

if __name__ == '__main__':
    cli()
