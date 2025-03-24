import subprocess
import os


def chimera_starten():
    insuline  = r"C:\Users\naomy\Downloads\pdb1a7f.ent" # deze is bij mij (gedownload) en dan insuline
    # je kan hier ook bijvoorbeeld boven ook alleen: '1a0m' invullen als losse string
    # wat een build-in ID is invullen en dan opent hij die.

    subprocess.run([r"C:\Program Files\ChimeraX 1.9\bin\chimerax.exe", insuline]) # hier opent hij chimera
    # via MIJN path dit verschilt wss met iedereen maarja kijken we wel naar, tweede argument
    # is puur voor het openen van een bepaald protein. als je deze weghaald opent hij gewoon chimera
    # de start pagina




chimera_starten()



