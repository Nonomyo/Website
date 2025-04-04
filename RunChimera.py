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
import os
import time

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

        if color != 'none':
            script_content += f" {color}\n"

        script_content += """movie record ; turn y 1 360 ; wait ; movie encode output static/video.mp4 ; quit
        """

        script_path = "static/temp_chimera.cxc"
        video_path = "static/video.mp4"

        if os.path.exists(video_path):
            os.remove(video_path)
            time.sleep(1)

        # Schrijf het scriptbestand
        with open(script_path, "w") as script_file:
            script_file.write(script_content)

        # Start ChimeraX en wacht tot het klaar is
        try:
            subprocess.run([self.chimera, '--script', script_path], check=True)

            # Wacht maximaal 10 seconden tot de video klaar is
            timeout = 10
            while not os.path.exists(video_path) and timeout > 0:
                time.sleep(1)
                timeout -= 1


        finally:
            if os.path.exists(script_path):
                os.remove(script_path)
