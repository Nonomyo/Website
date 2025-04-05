# **README**
  
BioVisualX  
Versie 3  
04-04-2025  
  
## BioVisualX
  
BioVisualX is een website waarop de gebruiker een eiwit-ID kan invoeren, die vervolgens wordt gekoppeld aan het bijpassende eiwit en wordt gevisualiseerd door middel van een 3D-animatie.
Het eiwit wordt hierbij weergegeven in de tertiaire structuur.
  
Hierdoor krijgt de gebruiker een goed en duidelijk beeld van het eiwit en de vormen ervan.  
Aan de hand van deze weergave van de vorm(en) van het eiwit kunnen verschillende functies van het eiwit worden verklaart.  
Een beter beeld van de vorm en functie kan ook zorgen voor meer duidelijkheid over de samenwerking tussen diverse eiwitten.

Voor het visualiseren van de eiwitten maakt BioVisualX gebruik van **UCSF ChimeraX**.  
**UCSF ChimeraX** is een programma voor de interactieve visualisatie en analyse van moleculaire structuren en gerelateerde gegevens.  
  
Dit is een voorbeeld van een mogelijke visualisatie:  
  
<img src="static/chimera_voorbeeld.png" alt="chimera output" width="400" height="250">
  
Op BioVisualX wordt er een animatie weergegeven die draait in plaats van een afbeelding.
  
De koppeling aan het eiwit en de visualisatie ervan zijn wel afhankelijk van de aanwezigheid van de data over het opgegeven  
eiwit in de PDB-database.  
Als er nog geen 3D-structuur van dit eiwit in de database bestaat en/of als het eiwit nog niet goed onderzocht is,
kan het zijn dat de koppeling en visualisatie niet mogelijk is.  
  
De website wordt gerunned via een Python file die gebruik maakt van **Flask**.  
**Flask** is een verzameling libraries en een Python-module waarmee eenvoudig een webapplicatie ontwikkeld kan worden.    
  
## Installatie instructies

### ChimeraX
  
Ga naar de volgende website voor de tool: https://www.cgl.ucsf.edu/chimerax/download.html
  
Kijk onder `ChimeraX version 1.9` en klik op `Other releases`.
  
Zoek naar Ubuntu 22.04 (Linux) en klik op de volgende link: `ucsf-chimerax_1.9ubuntu22.04_amd64.deb`.
  
Klik vervolgens op `Accept` onderaan het scherm, de tool begint nu met downloaden.
  
Volg nu de volgende stappen in de terminal om naar de `Downloads` folder te gaan: 
   
Om naar de "Downloads" folder te gaan: `cd Downloads`  
  
Check door middel van de volgende input of het installatieprogramma `ucsf-chimerax_1.9ubuntu22.04_amd64.deb` in de map staat: `ls`
    
Nu moet je jezelf toegang geven aan de tool, dit doe je door dit in de terminal te zetten:  
`chmod +x ucsf-chimerax_1.9ubuntu22.04_amd64.deb`  
    
Met `ls –l` zie je nu dat `ucsf-chimerax_1.9ubuntu22.04_amd64.deb` groen is geworden.  
    
Knip deze .deb map en plak deze in de `tool` map van de website.
  
Klik met de rechter muisknop op de .deb map en klik vervolgens op `Open with Ark`.
  
Druk op `Extract` en kies als locatie ook `tool`.
  
Hieruit komt een nieuwe map die dezelfde naam heeft als de .deb map.

Klik op deze map, knip de drie bestanden die hierin staan en plaats ook deze bestanden in `chimerax_map`.

Pak nu `data.tar.zst` uit door `Open with Ark` en selecteer ook hier als locatie `tool`.

In de uitgepakte `usr` map zit de map `bin` waarin ChimeraX zich bevindt.
  
Dit is waar het programma zich nu bevindt.
  
Het pad naar de tool is dus:
`tool/ucsf-chimerax_1.9ubuntu22.04_amd64/usr/bin/chimerax `
  
### Requirements
  
Het document 'requirements.txt' geeft weer welke libraries geïnstalleerd moeten worden om de website te kunnen gebruiken.  
  
Open dit bestand en tik in de terminal `pip install 'library'` in.
  
Vervang 'library' hierbij voor elke library die in het document staat.
  
Herhaal dit totdat alle libraries zijn geïnstalleerd.
  
## Gebruiksinstructie  

De website bestaat uit de volgende bestanden en mappen:  
  
- .idea
- brainstorm
- flask_session
- static
- templates
- tests
- tool
- README.md
- RunChimera.py
- app.py
- requirements.txt
  
Deze onderdelen zijn nodig om de website te laten werken.  
  
Na het volgen van de installatie instructies is alles nu gereed gemaakt.
  
Open het python bestand 'app.py' en run deze.
  
In de terminal komt nu een host adress te staan.
  
Kopieer of vul deze handmatig in in uw zoekbalk en de website zal vervolgens te voorschijn komen.
  
U kunt nu gebruik maken van de website door een eiwit-ID in te vullen, die de website voor u zal visualiseren!
  
## Contactgegevens
   
Fleur Luten - f.luten@st.hanze.nl  
Isa Bos - ir.bos.2@st.hanze.nl  
Naomy Schuppers - n.schuppers@st.hanze.nl  
Ype Vos - y.de.vos@st.hanze.nl  
  
## Licentieinformatie

In dit project hebben wij gebruik gemaakt van UCSF ChimeraX. ChimeraX is gebruikt voor het genereren van moleculaire visualisaties: https://www.cgl.ucsf.edu/chimerax/ 
