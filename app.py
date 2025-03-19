from flask import Flask, render_template, request
app = Flask(__name__)

# Dit is een lijst met titels voor alle pagina's op de website
titels = ['Super Coole Website', 'UCSF Chimera', 'BLAST', 'Help', 'About Us']

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


if __name__ == '__main__':
    app.run()

