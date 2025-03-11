from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('website.html')

@app.route('/blast_output')
def blast():
    return render_template('BLAST.html')

@app.route('/visualisation')
def chimera():
    return render_template('CHIMERA.html')

@app.route('/information')
def about_us():
    return render_template('ABOUT_US.html')

@app.route('/help_information')
def help():
    return render_template('HELP.html')

if __name__ == '__main__':
    app.run()
