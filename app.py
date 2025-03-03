from flask import Flask, render_template, request, redirect, url_for
from Bio.Blast import NCBIWWW, NCBIXML

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/nucleotide', methods=['GET', 'POST'])
def nucleotide():

@app.route('/amino', methods=['GET', 'POST'])
def amino():

@app.route('/protein', methods=['GET', 'POST'])
def protein():

@app.route('/chimera/<protein_id>')
def chimera(protein_id):

if __name__ == '__main__':
    app.run(debug=True)