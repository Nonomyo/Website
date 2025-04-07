"""
Tests voor RunChimera

Deze tests controleren of het script een video genereert met een geldig PDB-ID
en of een bestaande video correct wordt overschreven.

Auteurs: Ype de Vos, Isa Bos, Naomy Schuppers, Fleur Luten.
Versie: 1
Datum: 27-3-2025
"""

import os
import pytest
from tests.RunChimera import RunChimera
from tests.app import app

@pytest.fixture
def client():
    """
    Deze fixture creëert een testclient voor Flask om HTTP-verzoeken te simuleren.

    :param: None
    :return: client
    """
    with app.test_client() as client:
        # yield zorgt ervoor dat de client beschikbaar is voor de tests die deze fixture gebruiken.
        yield client
    

def test_video_generation(client):
    """
    Test of RunChimera een video genereert bij geldige input.
    Deze test gebruikt PDB-ID '1ABC' en kleur 'pink' en verwacht
    dat het bestand 'static/video.mp4' wordt aangemaakt.

    :param: client
    :return: None
    """

    video_path = "static/video.mp4"
    # als het path al bestaat, wordt deze verwijderd.
    if os.path.exists(video_path):
        os.remove(video_path)

    chimera = RunChimera()
    # neemt een voorbeeld ID en kleur als input.
    chimera.get_input("1ABC", "pink")
    # test of het path al bestaat
    assert os.path.exists("static/video.mp4"), "Video is niet gegenereerd."


def test_overwrite_video(client):
    """
    Test of een bestaande video wordt overschreven.
    Eerst wordt een test video gemaakt. Daarna wordt RunChimera uitgevoerd,
    en wordt er gecontroleerd of het bestand vervangen wordt door bestandsgrootte te vergelijken.

    :param: client
    :return: None
    """
    video_path = "static/video.mp4"

    # maakt een test video.
    with open(video_path, "w") as file:
        file.write("oude inhoud")

    old_size = os.path.getsize(video_path)

    # roept RunChimera aan.
    chimera = RunChimera()
    chimera.get_input("1ABC", "pink")

    # checkt de grootte van de video.
    new_size = os.path.getsize(video_path)

    assert os.path.exists(video_path), "De video bestaat helemaal niet."
    # checkt of de video dezelfde grootte heeft.
    assert new_size != old_size, "De video is niet goed overschreven."
