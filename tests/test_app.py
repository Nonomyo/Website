import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_homepage_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_homepage_inhoud(client):
    response = client.get("/")
    # Controleert of de titel van de pagina klopt.
    assert b"Super Coole Website" in response.data
    # Controleert of er een submit knop is; het invoeren van een Eiwit ID.
    assert b"type=\"submit\"" in response.data


def test_chimera_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_chimera_inhoud(client):
    response = client.get("/")
    # Controleert of de titel van de pagina klopt.
    assert b"UCSF Chimera" in response.data


def test_blast_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_blast_inhoud(client):
    response = client.get("/")
    # Controleert of de titel van de pagina klopt.
    assert b"BLAST" in response.data


def test_help_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_help_inhoud(client):
    response = client.get("/")
    # Controleert of de titel van de pagina klopt.
    assert b"Help" in response.data


def test_about_us_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_about_us_inhoud(client):
    response = client.get("/")
    # Controleert of de titel van de pagina klopt.
    assert b"About Us" in response.data


def test_error_status_code(client):
    response = client.get("/")
    assert response.status_code == 200

