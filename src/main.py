from fastapi import FastAPI, Depends
from routes.llm_router import router as llm_router
from routes.operations_router import router as operations_router
from utils import common_verificacao_api_token


app = FastAPI(
    title="Pós UFG APIs - Aula 2",
    description="API desenvolvida durante a aula 2 de da pós-graduação.",
    version="0.1",
    dependencies=[Depends(common_verificacao_api_token)],
)


app.include_router(llm_router, prefix="/llm")
app.include_router(operations_router, prefix="/operations")
