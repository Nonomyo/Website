"""
SUPER COOLE WEBSITE
versie 1
Bio-informatica leerjaar 1
Fleur Luten, Isa Bos, Naomy Schuppers, Yde de Vos

Deze code maakt gebruik van flask om een website met een eigen url te laten starten. De opdracht was om met HTML
CCS en Flask een werkende website te maken die een visualisatie kan maken. Onze website werkt met meerdere scripts,
HTML pagina's, CSS en code die samen werken om een goed werkende webiste te maken.
"""

from flask import Flask, render_template, request, jsonify, abort
from RunChimera import RunChimera
import cProfile
import pstats

app = Flask(__name__)


# Dit is een lijst met titels voor alle pagina's op de website
titels = [' BioVisualX', ' UCSF ChimeraX', ' Databases', ' Help', ' About Us', ' Output', 'Error']

@app.route('/', methods=['GET', 'POST'])
def home():
    error_message = None

    if request.method == 'POST':
        prot_id = request.form.get('prot_id', '')
        color = request.form.get('color', 'none')

#        if not prot_id:
#            return render_template("errorpage.html", titel=titels[6], error="errormesage.html")
#        if not prot_id:
#            abort(400)

        if len(prot_id) != 4:
            abort(400)




        chimera_start = RunChimera()
        chimera_start.get_input(prot_id, color=color)


        return render_template("output.html", prot_id=prot_id, titel=titels[5], video=True)

    return render_template("HOMEPAGE.html", titel=titels[0], error=error_message)

@app.errorhandler(400)
def page_not_found(error):
    """
    Function to catch and handle the 404 errors
    :param error:
    :return: rendered own defined 404.html
    """
    return render_template('errorpage.html'), 400

@app.route('/ChimeraX')
def chimera():
    """
    In deze functie staat de ChimeraX pagina.
    :return: CHIMERA.html met de titel 'UCSF ChimeraX'
    """
    return render_template(template_name_or_list = 'CHIMERA.html', titel = titels[1])

@app.route('/Databases')
def databases():
    """
    In deze functie staat de Databases pagina.
    :return: DATABASES.html met de titel 'Databases'
    """
    return render_template(template_name_or_list = 'DATABASES.html', titel = titels[2])

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


if __name__ == '__main__':
    app.run()
