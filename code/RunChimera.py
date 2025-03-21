from Bio.PDB import PDBList # For fetching the PDB file.

class RunChimera():
    def __init__(self, naam):
        self.pdb_file = naam



    def get_pdb(self):
        ''''
        this function will contain import methods from the Bio.PDB import.
        when given a pdb id, it wil fetch the corrosponding file from pdb.

        :param PDB id: a 4 digit sequence containing both letters and numbers.
        :return PDB file: a file containing a 3d structure of a protein.
        '''


    def read_pdb(self):
        ''''
        this function's importance is still questionable. if in some way to files
        have to be read to extract data, this function will be your guy.

        :param pdb file:
        :return ?:
        '''

    def run_chimera(self):
        ''''
        this function will catch the pdb file from the get_pdb function or the ? from the
        read_pdb function. the given information will be handed down to chimera to generate
        the 3d structure.

        :param pdb_file or ?: information that chimera needs to give back a 3d structure.
        :return 3d structure: a 3d structure of a protein.
        '''

    def make_image(self):
        ''''
        this function will generate an image of the 3d structure. image format is not yet decided.

        :param 3d structure: the 3d structure from chimera.
        :return image: an image of the 3d structure.
        '''

#    def __str__(self):
#        string = f'RunTool: {self.naam}' #voorbeeld


