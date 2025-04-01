"""
Test RunChimera
versie 1
Bio-informatica leerjaar 1
Fleur Luten, Isa Bos, Naomy Schuppers, Yde de Vos

In dit script worden alle functies in RunChimera.py getest met unittests. In RunChimera.py staat een class die ChimeraX
runt en een video maakt van het opgegeven eiwit die uiteindelijk op de website komt te staan.
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