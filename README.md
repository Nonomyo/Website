# README
  
De super coole website
Versie 2
11-03-2025
  
Een website die bestaande DNA sequentie van de gebruiker kan omzetten in een
aminozuursequentie, die vervolgens weer kan worden gekoppeld aan het bijpassende eiwit.
  
Hierbij wordt gebruik gemaakt van **BioPython**,**BLAST** en **UCSF ChimeraX**.  
**Biopython** is een verzameling van beschikbare Python modules voor computationele moleculaire biologie.  
**BLAST** staat voor Basic Local Alignment Search Tool. Het vindt regio's van gelijkenis tussen biologische sequenties.  
**UCSF ChimeraX** is een programma voor de interactieve visualisatie en analyse van moleculaire structuren en gerelateerde gegevens.  
  
Onderstaand is een voorbeeld weergegeven van de data over een sequentie die BioPython en BLAST terug kunnen geven.  
  
<img src="static/biopython_voorbeeld.png" alt="biopython en blast output" width="500" height="250">
  
Dit eiwit kan vervolgens door middel van **UCSF ChimeraX** worden gevisualiseerd in een 3D-weergave van de tertiaire- en mogelijk de  quarternaire structuur (afhankelijk van de hoeveelheid eiwitten).  
  
Dit is een voorbeeld van een mogelijke visualisatie:  
  
<img src="static/chimera_voorbeeld.png" alt="chimera output" width="500" height="250">
  
Aangezien een interactieve werking lastig is om goed te laten werken op de website,  
proberen wij een animatie weer te geven van het eiwit, zodat alle eigenschappen van het eiwit zichtbaar zijn.  
Net als in het bovenstaande voorbeeld, wordt de visualisatie van een eiwit op onze website gegarandeerd getoond als een afbeelding  
van de 3D-structuur.  
  
De koppeling aan het eiwit en de visualisatie ervan zijn wel afhankelijk van de aanwezigheid van de data over het opgegeven  
eiwit in de PDB-database.
Als er nog geen 3D-structuur van dit eiwit in de database bestaat en/of als het eiwit nog niet goed onderzocht is,  
kan het zijn dat de koppeling en visualisatie niet mogelijk is.  
  
De website wordt gerunned via een Python file die gebruik maakt van **Flask**.  
**Flask** is een verzameling libraries en een Python-module waarmee eenvoudig een webapplicatie ontwikkeld kan worden.    
  
## ChimeraX Linux installatie
  
Maak een map aan in de Linux terminal door gebruik te maken van de volgende invoer:
`cd ~`
`mkdir Documents/chimerax_map`
  
Ga naar de volgende website voor de tool: https://www.cgl.ucsf.edu/chimerax/download.html
  
Kijk onder "ChimeraX version 1.9" en klik op "Other releases".
  
Zoek naar Ubuntu 22.04 (Linux) en klik op de volgende link: "ucsf-chimerax_1.9ubuntu22.04_amd64.deb".
  
Klik vervolgens op “Accept” onderaan het scherm, de tool begint nu met downloaden.
  
Volg nu de volgende stappen in de terminal om naar de "Downloads" folder te gaan: 
   
Om naar de "Downloads" folder te gaan: `cd Downloads`  
  
Check door middel van de volgende input of het installatieprogramma "ucsf-chimerax_1.9ubuntu22.04_amd64.deb" in de map staat: `ls`
    
Nu moet je jezelf toegang geven aan de tool, dit doe je door dit in de terminal te zetten:  
`chmod +x ucsf-chimerax_1.9ubuntu22.04_amd64.deb`  
    
Met `ls –l` zie je nu dat "ucsf-chimerax_1.9ubuntu22.04_amd64.deb" groen is geworden.  
    
Knip deze .deb map en plak deze in "chimerax_map".
  
Klik met de rechter muisknop op de .deb map en klik vervolgens op "Open with Ark".
  
Druk op "Extract" en kies als locatie ook "chimerax_map".
  
Hieruit komt een nieuwe map die dezelfde naam heeft als de .deb map.

Klik op deze map, knip de drie bestanden die hierin staan en plaats ook deze bestanden in "chimerax_map".

Pak nu "data.tar.zst" uit door "Open with Ark" en selecteer ook hier als locatie "chimerax_map".

In de uitgepakte "usr" map zit de map "bin" waarin ChimeraX zich bevindt.
  
Dit is waar het programma zich nu bevindt.
  
Het hele pad vanaf de home map naar de tool is dus:
`~/Documents/chimerax_map/ucsf-chimerax_1.9ubuntu22.04_amd64/usr/bin/chimerax `
  
## Contactgegevens
  
Fleur Luten - f.luten@st.hanze.nl
Isa Bos - ir.bos.2@st.hanze.nl
Naomy Schuppers - n.schuppers@st.hanze.nl
Ype Vos - y.de.vos@st.hanze.nl

Referentie, Licenties


# Website
