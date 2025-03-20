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
app = Flask(__name__)

# Dit is een lijst met titels voor alle pagina's op de website
titels = ['Super Coole Website', 'UCSF Chimera', 'BLAST', 'Help', 'About Us', 'output']

@app.route('/', methods = ['GET', 'POST'])
def home():
    """
    In deze functie staan de Home Page en de Output.
    :return: HOMEPAGE.html of output.html met de titel 'Super Coole Website'
    """
    # Tot je iets invoerd zie je de "normale" Home Page.
    if request.method == 'GET':
        return render_template(template_name_or_list='HOMEPAGE.html', titel=titels[0])
    # Wanneer je een sequentie invoerd zie je een nieuwe pagina.
    elif request.method == 'POST':
        kwargs = {
            'fname' : request.form['fname'],
        }
        return render_template('output.html', **kwargs, titel=titels[0])

@app.route('/Chimera')
def chimera():
    """
    In deze functie staat de Chimera pagina.
    :return: CHIMERA.html met de titel 'UCSF Chimera'
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

@app.route('/Error')
def error():
    ''''
    in deze functie staat de error pagina.
    :return: ERROR.html met de titel 'Error'
    '''
    return render_template(template_name_or_list = 'error.html', titel = 'error')


if __name__ == '__main__':
    app.run()

