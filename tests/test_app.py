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
#     # Controleert of de header met de afbeelding aanwezig is.
#     assert b'<img src="../static/logo-hanze-oranje-zwart-rgb.png"' in response.data
#
#     # Controleert het navigatieschema.
#     assert b'href="/"' in response.data  # Home
#     assert b'href="/ChimeraX"' in response.data
#     assert b'href="/BLAST"' in response.data
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
    # Controleert of de header met de afbeelding aanwezig is.
    assert b'<img src="../static/logo-hanze-oranje-zwart-rgb.png"' in response.data

    # Controleert het navigatieschema.
    assert b'href="/"' in response.data  # Home
    assert b'href="/ChimeraX"' in response.data
    assert b'href="/BLAST"' in response.data
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


def test_blast(client):
    response = client.get("/BLAST")
    assert response.status_code == 200
    # Controleert of de titel van de pagina klopt.
    assert b"BLAST" in response.data

    # Ik laat deze even voor hoe hij is, omdat we nog niet zeker weten of we blast wel gaan gebruiken.


def test_databases(client):
    # Zorgt ervoor dat deze functie de Databases pagina controleert.
    response = client.get("/Databases")

    # 200 is de HTTP-status code voor OK, als de pagina het doet is het dus 200.
    assert response.status_code == 200

    # Controleert of de titel van de pagina klopt.
    assert b"Databases" in response.data
    # Controleert of de header met de afbeelding aanwezig is.
    assert b'<img src="../static/logo-hanze-oranje-zwart-rgb.png"' in response.data

    # Controleert het navigatieschema.
    assert b'href="/"' in response.data  # Home
    assert b'href="/ChimeraX"' in response.data
    assert b'href="/BLAST"' in response.data
    assert b'href="/Databases"' in response.data
    assert b'href="/Help"' in response.data
    assert b'href="/AboutUs"' in response.data

    # Controleert of de eerste h2-tag met de titel aanwezig is.
    assert b'Deze databases kan je gebruiken:</h2>' in response.data

    # Moeten we even afmaken als we info op de pagina hebben staan bij de databases.


def test_help(client):

    # Zorgt ervoor dat deze functie de Help pagina controleert.
    response = client.get("/Help")

    # 200 is de HTTP-status code voor OK, als de pagina het doet is het dus 200.
    assert response.status_code == 200

    # Controleert of de titel van de pagina klopt.
    assert b"Help" in response.data
    # Controleert of de header met de afbeelding aanwezig is.
    assert b'<img src="../static/logo-hanze-oranje-zwart-rgb.png"' in response.data

    # Controleert het navigatieschema.
    assert b'href="/"' in response.data  # Home
    assert b'href="/ChimeraX"' in response.data
    assert b'href="/BLAST"' in response.data
    assert b'href="/Databases"' in response.data
    assert b'href="/Help"' in response.data
    assert b'href="/AboutUs"' in response.data

    # Deze test moeten we verder uitbereiden als we de Help pagina af hebben.


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
    # Controleert of de header met de afbeelding aanwezig is.
    assert b'<img src="../static/logo-hanze-oranje-zwart-rgb.png"' in response.data

    # Controleert het navigatieschema.
    assert b'href="/"' in response.data  # Home
    assert b'href="/ChimeraX"' in response.data
    assert b'href="/BLAST"' in response.data
    assert b'href="/Databases"' in response.data
    assert b'href="/Help"' in response.data
    assert b'href="/AboutUs"' in response.data

    # Controleert of de h2-tag met de titel aanwezig is.
    assert b'<h2>Wie zijn wij?</h2>' in response.data
    # Controleert of de eerste zin van de tekst klopt.
    assert b"Welkom op onze website, (WEBSITE NAAM)." in response.data


def test_error(client):
    response = client.get("/")
    assert response.status_code == 200

    # Deze moeten we even aanpassen wanneer de error pagina af is, zodat we weten wat we moeten controleren.

