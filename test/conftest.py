import pytest

#Decorativo Fixture, te da algo listo para correr el test cuando lo necesite
@pytest.fixture
def numeros():
    return 5,5

