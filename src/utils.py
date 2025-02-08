import os
import logging

from dotenv import load_dotenv
from groq import Groq
from fastapi import HTTPException

load_dotenv()
API_TOKEN = int(os.getenv("API_TOKEN", 1234))
GROC_API_KEY = os.getenv("GROC_API_KEY")


def get_logger():
    """
    Cria e configura um logger para a aplicação FastAPI.

    Esta função configura o logger com nível de log INFO e define o formato das mensagens. Em seguida, retorna uma instância do logger identificada como 'fastapi'.

    Returns:
        logging.Logger: Instância configurada do logger.
    """
    logging.basicConfig(
        level=logging.INFO, format="[%(levelname)s] %(asctime)s - %(message)s"
    )
    return logging.getLogger("fastapi")


def common_verificacao_api_token(api_token: int):
    """
    Verifica se o token de API fornecido é válido.

    Parâmetros:
        api_token (int): Token de API fornecido para verificação.

    Exceções:
        HTTPException: Se o token fornecido não corresponder ao token esperado (API_TOKEN),
                       levantando uma exceção com status 401 e detalhe "Token inválido".
    """
    if api_token != API_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Token inválido",
        )


def executar_prompt(tema: str):
    """
    Gera uma história baseada no tema fornecido utilizando a API Groq.

    Args:
        tema (str): O tema sobre o qual a história será gerada.

    Returns:
        str: O conteúdo da história gerada pela API.

    Exemplo:
        historia = executar_prompt("aventura")
        print(historia)
    """
    prompt = f"Gerar história sobre o tema: {tema}"
    client = Groq(api_key=GROC_API_KEY)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.2-90b-vision-preview",
    )

    return chat_completion.choices[0].message.content
