
# calculadora.py

  
def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de dois números.

    Se o segundo número for zero, o Python irá gerar um erro.
    """
    return a / b

def potencia(a, b):
    """Retorna a potência de um numero"""
    return a ** b

def calcular_media(lista):
    """Retorna a media de uma lista"""
    if len(lista) == 0:
        raise ValueError("Não pode lista vazia")
    
    return sum(lista) / len(lista)