from fastapi import APIRouter
from utils import get_logger, executar_prompt

logger = get_logger()

router = APIRouter()


@router.post("/gerar_historia/", tags=["LLM"])
def gerar_historia(tema: str):
    """
    Gera uma história baseada no tema informado, registrando o processo e retornando o resultado.

    Parâmetros:
        tema (str): O tema que servirá de base para a criação da história.

    Retorna:
        dict: Um dicionário contendo a história gerada, onde a chave "historia" mapeia o conteúdo produzido.
    """
    logger.info(f"Tema informado: {tema}")
    return {"historia": executar_prompt(tema)}
