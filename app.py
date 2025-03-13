from flask import Flask, render_template
app = Flask(__name__)

titels = ['Super Coole Website', 'UCSF Chimera', 'BLAST', 'Help', 'About Us']

@app.route('/')
def home():
    return render_template(template_name_or_list = 'HOMEPAGE.html', titel = titels[0])

@app.route('/Chimera')
def chimera():
    return render_template(template_name_or_list = 'CHIMERA.html', titel = titels[1])

@app.route('/BLAST')
def blast():
    return render_template(template_name_or_list = 'BLAST.html', titel = titels[2])

@app.route('/Help')
def help():
    return render_template(template_name_or_list = 'HELP.html', titel = titels[3])

@app.route('/AboutUs')
def about_us():
    return render_template(template_name_or_list = 'ABOUT_US.html', titel = titels[4])


if __name__ == '__main__':
    app.run()

