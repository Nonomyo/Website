""""
RunChimera

authors: Ype de Vos, Isa Bos, Naomy Schuppers, Fleur Luten.
versie 1.
date: 27-3-2025

This script contains a class that asks the user to submit a pdb id. The class
will use this pdb id to search through the pdb database for a file about the
corresponding protein. This file, along with a csc file containing instruction,
will be given to chimerax to generate an animation of the 3d structure of the protein.
"""
import subprocess

class RunChimera:
    def __init__(self):
        self.chimera = r"C:\Program Files\ChimeraX 1.9\bin\ChimeraX.exe"

    def get_input(self, pdb_id, color=None):
        """
        Start ChimeraX met het opgegeven PDB ID en maak een 3D-animatie.

        :param pdb_id: Een 4-letterige PDB-ID (bijv. '1ABC').
        :param color: Kleur die wordt toegepast (bijvoorbeeld 'pink'). Als None, wordt geen kleur toegevoegd.
        """
        script_content = f"open {pdb_id}\n"

        # Voeg de kleurregel toe als de parameter niet None is
        if color != 'none':  # Alleen als de gebruiker een kleur kiest
            script_content += f" {color}\n"


        # Voeg de animatie en video-encoding regels toe
        script_content += """movie record ; turn y 1 360 ; wait ; movie encode output static/video.mp4 ; quit
        """

        script_path = "static/temp_chimera.cxc"

        # Schrijf het script naar het bestand
        with open(script_path, "w") as script_file:
            script_file.write(script_content)

        # Start ChimeraX met het script
        subprocess.run([self.chimera, '--script', script_path])






