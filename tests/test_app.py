import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200

def test_homepage_inhoud(client):
    response = client.get("/")
    # Controleert of de titel van de homepage klopt.
    assert b"Super Coole Website" in response.data
    # Controleert of er een submit knop is; het invoeren van een Eiwit ID.
    assert b"type=\"submit\"" in response.data

