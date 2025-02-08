from fastapi import Depends, HTTPException, status, APIRouter

from utils import get_logger
from models import NomeGrupo, Numero, Resultado, TipoOperacao
from utils import common_verificacao_api_token

logger = get_logger()
router = APIRouter()


@router.get(
    "/teste",
    summary="Hello world!",
    tags=[NomeGrupo.teste],
    dependencies=[Depends(common_verificacao_api_token)],
)
def hello_world():
    return {"message": "hello world"}


@router.post(
    "/soma/v1/{num1}/{num2}",
    summary="Soma dois números",
    tags=[NomeGrupo.operacoes],
    dependencies=[Depends(common_verificacao_api_token)],
)
def soma(num1: int, num2: int):
    return {"resultado": num1 + num2}


@router.post(
    "/soma/v2",
    summary="Soma dois números por query params",
    tags=[NomeGrupo.operacoes],
    response_model=Resultado,
)
def soma(num1: int, num2: int):
    total = num1 + num2
    return {"resultado": total, "outra_info": "teste"}


@router.post(
    "/soma/v3",
    summary="Soma dois números por body",
    description="Recebe dois números e retorna a soma.",
    status_code=status.HTTP_200_OK,
    tags=[NomeGrupo.operacoes],
)
def soma(num: Numero) -> Resultado:
    total = num.num1 + num.num2

    if total < 0:
        logger.error("Deu erro!!")

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Resultado negativo não é permitido.",
        )
    logger.info("Soma efetuada com sucesso!")
    return {"resultado": num.num1 + num.num2}


@router.post("/operacao", tags=[NomeGrupo.operacoes])
def operacao(numero: Numero, tipo: TipoOperacao):
    if tipo == TipoOperacao.soma:
        total = numero.num1 + numero.num2
    elif tipo == TipoOperacao.subtracao:
        total = numero.num1 - numero.num2
    elif tipo == TipoOperacao.divisao:
        total = numero.num1 / numero.num2
    elif tipo == TipoOperacao.multiplicacao:
        total = numero.num1 * numero.num2

    logger.info("Requisição efetuada com sucesso!")
    return {"resultado": total}
