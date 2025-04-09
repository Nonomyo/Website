""""
RunChimera

Auteurs: Ype de Vos, Isa Bos, Naomy Schuppers, Fleur Luten.
Versie: 1
Datum: 09-04-2025

In dit script staat een class die de gebruiker verschillende opties geeft voor het uitvoeren van de website
met gebruik van de tool ChimeraX. Er worden verschillende argumenten gegeven voor het runnen van ChimeraX
en het maken van een 360 graden video van het opgegeven ID met de gekozen eisen.
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

        # De kleur die de animatie krijgt.
        if color != 'none':
            script_content += f" {color}\n"

        # Dit is nodig voor het maken van de video
        script_content += """movie record ; turn y 1 360 ; wait ; movie encode output static/video.mp4 ; quit
        """

        # Path voor het maken van de video
        script_path = "static/temp_chimera.cxc"
        video_path = "static/video.mp4"

        if os.path.exists(video_path):
            os.remove(video_path)
            time.sleep(1)

        # Schrijf het scriptbestand voor het maken van de video
        with open(script_path, "w") as script_file:
            script_file.write(script_content)

        # Start ChimeraX en wacht de video is gemaakt
        try:
            subprocess.run([self.chimera, '--script', script_path], check=True)

            timeout = 10
            while not os.path.exists(video_path) and timeout > 0:
                time.sleep(1)
                timeout -= 1

        finally:
            if os.path.exists(script_path):
                os.remove(script_path)
