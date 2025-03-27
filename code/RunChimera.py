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


class RunChimera():
    def __init__(self, user_input):
        self.chimera = r"C:\Program Files\Chimera 1.19\bin\chimera.exe"
        self.user_input = user_input



    def get_input(self, pdb_id):
        ''''
        This function will collect a pdb id as input and search through the pdb
        database for the corresponding protein. next, this function will start
        chimera to show an animation of the 3d structure of the protein.

        :param pdb_id: a 4 digit sequence containing both letters and numbers.
        :return protein structure: a 3d structure of the protein.
        '''

        self.user_input = pdb_id
        huidig_script = f"""open {pdb_id} 
        movie record ; turn y 1 360 ; wait ; movie encode output video.mp4
        """
        script_path = "temp_chimera.cxc"
        with open(script_path, "w") as script_file:
            script_file.write(huidig_script)
        subprocess.run([r"C:\Program Files\ChimeraX 1.9\bin\ChimeraX.exe", '--script', script_path])


    def __str__(self):

        return f'running chimera with pdb_id: {[self.get_input]}' #voorbeeld


test = RunChimera(input)
test.get_input(input('prot id; '))