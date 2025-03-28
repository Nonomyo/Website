"""
SUPER COOLE WEBSITE
versie 1
Bio-informatica leerjaar 1
Fleur Luten, Isa Bos, Naomy Schuppers, Yde de Vos
Deze code maakt gebruik van flask om een website met een eigen url te laten starten. De opdracht was om met HTML
CCS en Flask een werkende website te maken die een visualisatie kan maken. Onze website werkt met meerdere scripts,
HTML pagina's, CSS en code die samen werken om een goed werkende webiste te maken.
"""

from flask import Flask, render_template, request
from RunChimera import RunChimera


app = Flask(__name__)

# Dit is een lijst met titels voor alle pagina's op de website
titels = ['Super Coole Website', 'UCSF ChimeraX', 'BLAST', 'Help', 'About Us', 'Output', 'Error']

@app.route('/', methods=['GET', 'POST'])
def home():
    error_message = None
    if request.method == 'POST':
        prot_id = request.form.get('prot_id', '')

        if not prot_id:
            return render_template("errorpage.html", titel=titels[6], error="errormesage.html")

        chimera_start = RunChimera()
        chimera_start.get_input(prot_id)

        return render_template("output.html", prot_id=prot_id, titel=titels[5], video=True)

    return render_template("HOMEPAGE.html", titel=titels[0], error=error_message)

@app.route('/ChimeraX')
def chimera():
    """
    In deze functie staat de ChimeraX pagina.
    :return: CHIMERA.html met de titel 'UCSF ChimeraX'
    """
    return render_template(template_name_or_list = 'CHIMERA.html', titel = titels[1])

@app.route('/BLAST')
def blast():
    """
    In deze functie staat de Blast pagina.
    :return: BLAST.html met de titel 'BLAST'
    """
    return render_template(template_name_or_list = 'BLAST.html', titel = titels[2])

@app.route('/Help')
def help():
    """
    In deze functie staat de help pagina.
    :return: HELP.html met de titel 'Help'
    """
    return render_template(template_name_or_list = 'HELP.html', titel = titels[3])

@app.route('/AboutUs')
def about_us():
    """
    In deze functie staat de About Us pagina.
    :return: ABOUT_US.html met de titel 'About Us'
    """
    return render_template(template_name_or_list = 'ABOUT_US.html', titel = titels[4])

@app.route('/make-pink', methods=['POST'])
def make_pink():
    global is_pink
    is_pink = True  # Zet de knop roze
    return render_template('index.html', is_pink=is_pink)




if __name__ == '__main__':
    app.run()
