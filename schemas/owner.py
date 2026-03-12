from pydantic import BaseModel
from typing import Optional, List
from model.owner import Owner

class OwnerSchema(BaseModel):
    """ Define como um novo proprietário a ser inserido deve ser representado
    """
    name: str = "John Doe"
    email: str = "john.doe@example.com"
    phone: str = "1234567890"
    password: str = "password123"


class OwnerSearchSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do proprietário.
    """
    name: str = "John Doe"


class ListOwnersSchema(BaseModel):
    """ Define como uma listagem de proprietários será retornada.
    """
    owners: List[OwnerSchema]


def show_owners(owners: List[Owner]):
    """ Retorna uma representação do proprietário seguindo o schema definido em
        OwnerViewSchema.
    """
    result = []
    for owner in owners:
        result.append({
            "name": owner.name,
            "email": owner.email,
            "phone": owner.phone,
        })

    return {"owners": result}


class OwnerViewSchema(BaseModel):
    """ Define como um proprietário será retornado: proprietário + comentários.
    """
    id: int = 1
    name: str = "John Doe"
    email: str = "john.doe@example.com"
    phone: str = "1234567890"


class OwnerDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    name: str

def show_owner(owner: Owner):
    """ Retorna uma representação do proprietário seguindo o schema definido em
        OwnerViewSchema.
    """
    return {
        "id": owner.id,
        "name": owner.name,
        "email": owner.email,
        "phone": owner.phone
    }