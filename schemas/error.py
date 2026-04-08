from pydantic import BaseModel

class ErrorSchema400(BaseModel):
    """ Define como o erro de bad request será representado.
    """
    mesage: str = "Bad request"

class ErrorSchema404(BaseModel):
    """ Define como o erro de recurso não encontrado será representado.
    """
    mesage: str = "Recurso não encontrado"

class ErrorSchema409(BaseModel):
    """ Define como o erro de registro duplicado na base de dados.
    """
    mesage: str = "Registro já existe na base de dados"