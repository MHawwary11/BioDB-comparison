import os
from flask import Flask, flash, request, redirect, url_for, render_template
from DBCV.analysis import compare_data


app = Flask(__name__)


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)
DATA_FILES = os.path.join(BASE_DIR,'project_package','data')
os.chdir(DATA_FILES)




@app.route("/")
def home():
    """
    This method loads the home page with the comparison table between the two databases

    """
    df=compare_data('new_out.tsv')
    df=df.to_html(index=False)
    return render_template('template.html',DF=df)

@app.route("/protein", methods=['POST'])
def protein():
    """
    This method is responsible for displaying the comparison between the two databases for a specific protein written
    in the textbox of the GUI

    """
    summary = compare_data('new_out.tsv')
    summary = summary.to_html(index=False)
    protein_name=request.form['textbox']
    df=compare_data('new_out.tsv',protein_name)
    if df is not None:

        uniprot_seq=df.iloc[4,1]
        if len(uniprot_seq) >30:
          uniprot_seq=uniprot_seq[:30]+'...'
        refseq_seq=df.iloc[4,2]
        if len(refseq_seq)>30:
            refseq_seq=refseq_seq[:30]+'...'

        df.iloc[4,1]=uniprot_seq
        df.iloc[4,2]=refseq_seq

        df=df.to_html(index=False)

    return render_template('template.html',comp=df,DF=summary)


if __name__ == '__main__':
    app.run(debug=True)

