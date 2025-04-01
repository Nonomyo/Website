"""
Test website html
versie 1
Bio-informatica leerjaar 1
Fleur Luten, Isa Bos, Naomy Schuppers, Yde de Vos

In dit script worden alle functies in de app.py getest met unittests. In app.py staan de html pagina's van de website.
Vooral de opmaak van de website wordt dus in dit script getest.
"""

import pytest
from app import app


@pytest.fixture
def client():
    """
    Deze functie is een fixture, hiermee wordt een herbruikbaar object (client) aangemaakt om te gebruiken voor
    het testen van functies met pytest.
    :return: test client
    """
    with app.test_client() as client:
        # yield zorgt ervoor dat de client beschikbaar is voor de tests die deze fixture gebruiken.
        yield client


# De tests van de homepage heb ik even uit gezet, omdat de homepage heel wat is veranderd en nog gaat veranderen.


# def test_homepage(client):
#     """
#     In deze test functie wordt de homepage van de website gecontroleerd.
#     Er wordt getest of de volgende onderdelen aanwezig zijn/werken:
#     - Header: titel van de pagina en afbeelding
#     - Navigatieschema
#     - Submit knop om een Eiwit ID in te voeren
#     - Titel van de tekst en de eerste zin van de tekst
#
#     :param client: test client om de functie te testen
#     :return: een pass als de functie doet wat hij moet doen en een error als dit niet zo is.
#     """
#
#     # Zorgt ervoor dat deze functie de root controleerd, voor ons de homepage.
#     response = client.get("/")
#
#     # 200 is de HTTP-status code voor OK, als de pagina het doet is het dus 200.
#     assert response.status_code == 200
#
#     # Controleert of de titel van de pagina klopt.
#     assert b"Super Coole Website" in response.data
#     # Controleert of de header met de afbeeldingen aanwezig zijn.
#     assert b'<img src="../static/logo biovisualx.jpeg" height="100" width="120"/>' in response.data
#     assert b'<img src="../static/logo biovisualx spiegel.png" height="100" width="120"/>' in response.data
#      # Controleert het navigatieschema.
#     assert b'href="/"' in response.data  # Home
#     assert b'href="/ChimeraX"' in response.data
#     assert b'href="/Databases"' in response.data
#     assert b'href="/Help"' in response.data
#     assert b'href="/AboutUs"' in response.data
#
#     # Controleert of er een submit knop is; het invoeren van een Eiwit ID.
#     assert b"type=\"submit\"" in response.data
#     # Controleert de zoek knop.
#     assert b'input type="text" id="prot_id" name="prot_id"' in response.data
#
#     # Controleert of de h2-tag met de titel aanwezig is.
#     assert b'<h2>WEBSITE NAAM?</h2>' in response.data
#     # Controleert of de eerste zin van de tekst klopt.
#     assert b"Welkom bij onze website voor het vertalen en informeren van eiwitten." in response.data


# def test_homepage_post_request(client):
#     response = client.post("/", data={"prot_id": "test"})
#     assert response.status_code == 200
#     assert b"test" in response.data
#
#     # Deze test moet aangepast worden als we weten hoe de input en output er uit gaat zien.
#     # Hier heb ik even de basis opgeschreven, zodat we het niet vergeten.


def test_chimera(client):
    """
       In deze test functie wordt de ChimeraX pagina van de website gecontroleerd.
       Er wordt getest of de volgende onderdelen aanwezig zijn/werken:
       - Header: titel van de pagina en afbeelding
       - Navigatieschema
       - Titel van de tekst en de eerste zin van de tekst (voor 2 tekstdelen)
       - Afbeelding Chimera Logo

       :param client: test client om de functie te testen
       :return: een pass als de functie doet wat hij moet doen en een error als dit niet zo is.
       """

    # Zorgt ervoor dat deze functie de ChimeraX pagina controleert.
    response = client.get("/ChimeraX")

    # 200 is de HTTP-status code voor OK, als de pagina het doet is het dus 200.
    assert response.status_code == 200

    # Controleert of de titel van de pagina klopt.
    assert b"UCSF ChimeraX" in response.data
    # Controleert of de header met de afbeeldingen aanwezig zijn.
    assert b'<img src="../static/logo biovisualx.jpeg" height="100" width="120"/>' in response.data
    assert b'<img src="../static/logo biovisualx spiegel.png" height="100" width="120"/>' in response.data

    # Controleert het navigatieschema.
    assert b'href="/"' in response.data  # Home
    assert b'href="/ChimeraX"' in response.data
    assert b'href="/Databases"' in response.data
    assert b'href="/Help"' in response.data
    assert b'href="/AboutUs"' in response.data

    # Controleert of de eerste h2-tag met de titel aanwezig is.
    assert b'<h2>Wat is UCSF ChimeraX?</h2>' in response.data
    # Controleert of de eerste zin van de tekst klopt.
    assert (b"Voor het maken van deze website hebben we onder andere gebruik gemaakt van de tool UCSF ChimeraX."
            in response.data)

    # Controleert of de tweede h2-tag met de titel aanwezig is.
    assert b'<h2>Waar hebben wij UCSF ChimeraX voor gebruikt?</h2>' in response.data
    # Controleert of het eerste deel van de eerste zin van de tekst klopt.
    assert (b"Door middel van UCSF Chimera hebben we genetische data kunnen omzetten naar visuele data,"
            in response.data)

    # Controleert of de afbeelding van chimera aanwezig is.
    assert b'<img src="../static/ucsf-chimera.png"' in response.data


def test_databases(client):
    """
       In deze test functie wordt de Databases pagina van de website gecontroleerd.
       Er wordt getest of de volgende onderdelen aanwezig zijn/werken:
       - Header: titel van de pagina en afbeelding
       - Navigatieschema
       - Titel van de tekst en de eerste zin van de tekst
       - Titel, link naar website en eerste zin van de tekst per database

       :param client: test client om de functie te testen
       :return: een pass als de functie doet wat hij moet doen en een error als dit niet zo is.
    """

    # Zorgt ervoor dat deze functie de Databases pagina controleert.
    response = client.get("/Databases")

    # 200 is de HTTP-status code voor OK, als de pagina het doet is het dus 200.
    assert response.status_code == 200

    # Controleert of de titel van de pagina klopt.
    assert b"Databases" in response.data
    # Controleert of de header met de afbeeldingen aanwezig zijn.
    assert b'<img src="../static/logo biovisualx.jpeg" height="100" width="120"/>' in response.data
    assert b'<img src="../static/logo biovisualx spiegel.png" height="100" width="120"/>' in response.data

    # Controleert het navigatieschema.
    assert b'href="/"' in response.data  # Home
    assert b'href="/ChimeraX"' in response.data
    assert b'href="/Databases"' in response.data
    assert b'href="/Help"' in response.data
    assert b'href="/AboutUs"' in response.data

    # Controleert of de eerste h2-tag met de titel aanwezig is.
    assert b'Waarom Databases?</h2>' in response.data
    # Controleert of het eerste deel van de eerste zin van de tekst klopt.
    assert b"ChimeraX maakt gebruik van verschillende databases" in response.data

    # Controleert of de UniProt h2-tag met de titel aanwezig is.
    assert b'UniProt:</h2>' in response.data
    # Controleert of de link naar UniProt aanwezig is
    assert b'<a href="https://www.uniprot.org/" target="_blank">UniProt</a>' in response.data
    # Controleert of het eerste deel van de eerste zin van de tekst klopt.
    assert b'is een uitgebreide database' in response.data

    # Controleert of de AlphaFold h2-tag met de titel aanwezig is.
    assert b'AlphaFold:</h2>' in response.data
    # Controleert of de link naar AlphaFold aanwezig is
    assert b'<a href="https://alphafold.ebi.ac.uk/" target="_blank">AlphaFold</a>' in response.data
    # Controleert of het eerste deel van de eerste zin van de tekst klopt.
    assert b'biedt voorspelde eiwitstructuren' in response.data

    # Controleert of de EMDB h2-tag met de titel aanwezig is.
    assert b'EMDB (Electron Microscopy Data Bank):</h2>' in response.data
    # Controleert of de link naar EMBD aanwezig is
    assert b'<a href="https://www.ebi.ac.uk/emdb/" target="_blank">EMDB</a>' in response.data
    # Controleert of het eerste deel van de eerste zin van de tekst klopt.
    assert b'bevat cryo-elektronmicroscopie' in response.data

    # Controleert of de ModelArchive h2-tag met de titel aanwezig is.
    assert b'ModelArchive:</h2>' in response.data
    # Controleert of de link naar ModelArchive aanwezig is
    assert b'<a href="https://modelarchive.org/" target="_blank">ModelArchive</a>' in response.data
    # Controleert of het eerste deel van de eerste zin van de tekst klopt.
    assert b'slaat theoretische en computationele' in response.data

    # Controleert of de PubChem h2-tag met de titel aanwezig is.
    assert b'PubChem:</h2>' in response.data
    # Controleert of de link naar PubChem aanwezig is
    assert b'<a href="https://pubchem.ncbi.nlm.nih.gov/" target="_blank">PubChem</a>' in response.data
    # Controleert of het eerste deel van de eerste zin van de tekst klopt.
    assert b'is een database met' in response.data

    # Controleert of de RCSB PDB h2-tag met de titel aanwezig is.
    assert b'RCSB PDB:</h2>' in response.data
    # Controleert of de link naar PubChem aanwezig is
    assert b'<a href="https://www.rcsb.org/" target="_blank">RCSB</a>' in response.data
    # Controleert of het eerste deel van de eerste zin van de tekst klopt.
    assert b'is een databank die wetenschappelijke doorbraken' in response.data


def test_help(client):
    """
        In deze test functie wordt de Help van de website gecontroleerd.
        Er wordt getest of de volgende onderdelen aanwezig zijn/werken:
        - Header: titel van de pagina en afbeelding
        - Navigatieschema
        - Titel van de tekst en de eerste zin van de tekst (voor elk tekst deel)
        - Afbeeldingen

        :param client: test client om de functie te testen
        :return: een pass als de functie doet wat hij moet doen en een error als dit niet zo is.
    """

    # Zorgt ervoor dat deze functie de Help pagina controleert.
    response = client.get("/Help")

    # 200 is de HTTP-status code voor OK, als de pagina het doet is het dus 200.
    assert response.status_code == 200

    # Controleert of de titel van de pagina klopt.
    assert b"Help" in response.data
    # Controleert of de header met de afbeeldingen aanwezig zijn.
    assert b'<img src="../static/logo biovisualx.jpeg" height="100" width="120"/>' in response.data
    assert b'<img src="../static/logo biovisualx spiegel.png" height="100" width="120"/>' in response.data

    # Controleert het navigatieschema.
    assert b'href="/"' in response.data  # Home
    assert b'href="/ChimeraX"' in response.data
    assert b'href="/Databases"' in response.data
    assert b'href="/Help"' in response.data
    assert b'href="/AboutUs"' in response.data

    # Controleert of de eerste h2-tag met de titel aanwezig is.
    assert b'Instructies nodig?</h2>' in response.data
    # Controleert of het eerste deel van de eerste zin van de tekst klopt.
    assert b"Onze website werkt heel simpel en effectief voor u." in response.data

    # Controleert of de tweede h2-tag met de titel aanwezig is.
    assert b'Wil je deze visualisatie downloaden?</h2>' in response.data
    # Controleert of het eerste deel van de eerste zin van de tekst klopt.
    assert b"Het is mogelijk om deze 3D visualisatie te downloaden" in response.data

    # Controleert of de afbeeldingen aanwezig zijn
    assert b'<img src="../static/drie_puntjes.png" height="254" width="414"/>' in response.data
    assert b'<img src="../static/download help .png" height="328" width="416"/>' in response.data


def test_about_us(client):
    """
        In deze test functie wordt de About Us van de website gecontroleerd.
        Er wordt getest of de volgende onderdelen aanwezig zijn/werken:
        - Header: titel van de pagina en afbeelding
        - Navigatieschema
        - Titel van de tekst en de eerste zin van de tekst

        :param client: test client om de functie te testen
        :return: een pass als de functie doet wat hij moet doen en een error als dit niet zo is.
        """

    # Zorgt ervoor dat deze functie de About Us pagina controleert.
    response = client.get("/AboutUs")

    # 200 is de HTTP-status code voor OK, als de pagina het doet is het dus 200.
    assert response.status_code == 200

    # Controleert of de titel van de pagina klopt.
    assert b"About Us" in response.data
    # Controleert of de header met de afbeeldingen aanwezig zijn.
    assert b'<img src="../static/logo biovisualx.jpeg" height="100" width="120"/>' in response.data
    assert b'<img src="../static/logo biovisualx spiegel.png" height="100" width="120"/>' in response.data

    # Controleert het navigatieschema.
    assert b'href="/"' in response.data  # Home
    assert b'href="/ChimeraX"' in response.data
    assert b'href="/Databases"' in response.data
    assert b'href="/Help"' in response.data
    assert b'href="/AboutUs"' in response.data

    # Controleert of de h2-tag met de titel aanwezig is.
    assert b'<h2>Wie zijn wij?</h2>' in response.data
    # Controleert of de eerste zin van de tekst klopt.
    assert b"Welkom op onze website" in response.data


def test_error(client):
    response = client.get("/")
    assert response.status_code == 200

    # Deze moeten we even aanpassen wanneer de error pagina af is, zodat we weten wat we moeten controleren.

