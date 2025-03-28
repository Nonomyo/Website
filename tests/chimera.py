import subprocess

def chimera_starten():
    protein = input("Voer id in: ") #voor ons voor een input

   # dit is de inhoud van het tijdelijke script
    script_inhoud_tijdelijk = f"""open {protein} 
movie record ; turn y 1 360 ; wait ; movie encode output video.mp4

"""

    script_path = "../temp_chimerax.cxc"  # hij maakt hier het tekst bestand (.cxc) voor het tijdelijke script
    with open(script_path, "w") as script_file: # opent het tijdelijke script in write modes
        script_file.write(script_inhoud_tijdelijk) # zet de tijdelijke inhoud in het script

    subprocess.run([r"C:\Program Files\ChimeraX 1.9\bin\chimerax.exe","--script", script_path]) # voert het uit



chimera_starten()







