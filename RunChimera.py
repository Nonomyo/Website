""""
RunChimera
versie 1
Bio-informatica leerjaar 1
Fleur Luten, Isa Bos, Naomy Schuppers, Yde de Vos

In dit script staat een class die met het opgegeven eiwit ID en ChimeraX een video maakt van dit eiwit. Hier zijn
verschillende opties bij mogelijk, die de gebruiker kan opgeven. De video komt op de website te staan.
"""

import subprocess

class RunChimera:
    def __init__(self):
        self.chimera = r"C:\Program Files\ChimeraX 1.9\bin\ChimeraX.exe"

    def get_input(self, pdb_id):
        """
        Start ChimeraX met het opgegeven PDB ID en maak een 3D-animatie.

        :param pdb_id: Een 4-letterege PDB-ID (bijv. '1ABC').
        """
        script_content = f"""open {pdb_id} 
        movie record ; turn y 1 360 ; wait ; movie encode output static/video.mp4 ; quit
        """
        script_path = "static/temp_chimera.cxc"
        with open(script_path, "w") as script_file:
            script_file.write(script_content)

        subprocess.run([self.chimera, '--script', script_path])
