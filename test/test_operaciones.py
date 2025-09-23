import pytest
import calculadora


def test_sumar():
    assert calculadora.sumar(2,4) == 6 #todo lo que viene despues de assert tiene que ser el resultado esperado

def test_restar():
    assert calculadora.restar(10, 3) == 7

def test_multiplicar():
    assert calculadora.multiplicar(3, 5) == 15

def test_dividir():
    assert calculadora.dividir(8, 2) == 4

def test_dividir_por_cero_levanta_error():
    with pytest.raises(ValueError): #raises sirve para devolverme expresiones de errores
        calculadora.dividir(5, 0)

#Decoradores: nos permiten hacer varias pruebas/ evalua varios casos al mismo tiempo
@pytest.mark.parametrize("a,b,esperado",[
    (2,5,7), #Evaluar numeros positivos
    (-4,-2,-6), #numeros negativos
    (0,0,0) #numeros ceros
])
def test_sumar_varios(a,b,esperado):
    assert calculadora.sumar(a,b) == esperado

#Mark personalizados en el archivo pytest.ini
@pytest.mark.listo

#pruebas usando un fixture ya creado
def test_restar_con_fixture(numeros):
    a,b = numeros
    assert calculadora.restar(a,b) == 0

def test_sumar_con_fixture(numeros):
    a,b = numeros
    assert calculadora.sumar(a,b) == 10

