from enum import Enum
from pydantic import BaseModel, PositiveInt


class NomeGrupo(str, Enum):
    """
    Enumeração que representa os nomes dos grupos.

    Atributos:
        operacoes (str): Representa o grupo "Operações matemágicas".
        teste (str): Representa o grupo "Teste".
    """

    operacoes = "Operações matemágicas"
    teste = "Teste"


class Numero(BaseModel):
    """
    Classe Numero que representa um modelo de dados com dois números inteiros positivos.

    Atributos:
        num1 (PositiveInt): O primeiro número inteiro positivo.
        num2 (PositiveInt): O segundo número inteiro positivo.
    """

    num1: PositiveInt
    num2: PositiveInt


class Resultado(BaseModel):
    """
    Classe que representa o resultado de uma operação.

    Atributos:
        resultado (int): O valor do resultado da operação.
    """

    resultado: int


class TipoOperacao(str, Enum):
    """
    Enumeração que representa os tipos de operações matemáticas.

    Atributos:
        soma (str): Representa a operação de soma.
        subtracao (str): Representa a operação de subtração.
        divisao (str): Representa a operação de divisão.
        multiplicacao (str): Representa a operação de multiplicação.
    """

    soma = "soma"
    subtracao = "subtracao"
    divisao = "divisao"
    multiplicacao = "multiplicacao"
