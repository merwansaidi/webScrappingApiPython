from flask import Flask
from flask import render_template

# import du fichier de donnees
import Playerdataviz as pdv

app = Flask(__name__)

@app.route('/')

def index():
    meilleursDribbleurs = pdv.topSkills(20, 'dribbling')
    meilleursPasseurs = pdv.topSkills(20, 'passing')
    meilleursTireurs = pdv.topSkills(20, 'shooting')
    return render_template("index.html", dribbleurs = meilleursDribbleurs.to_html(), passeurs = meilleursPasseurs.to_html(), tireurs = meilleursTireurs.to_html())

if __name__ == "__main__":
    app.run(debug = True)