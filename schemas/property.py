from pydantic import BaseModel
from typing import Optional, List
from model.owner import Owner
from datetime import datetime

from model.property import Property

class PropertySchema(BaseModel):
    """ Define como uma nova propriedade a ser inserida deve ser representada
    """
    title: str
    value: float
    type: str
    owner_id: int
    address: str
    status: str
    area: int
    rooms: int
    bathrooms: int

class PropertySearchSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da propriedade.
    """
    title: str = "Casa dos Sonhos"


class ListPropertiesSchema(BaseModel):
    """ Define como uma listagem de propriedades será retornada.
    """
    properties: List[PropertySchema]


def show_properties(properties: List[Property]):
    """ Retorna uma representação da propriedade seguindo o schema definido em
        PropertyViewSchema.
    """
    result = []
    for property in properties:
        result.append({
            "title": property.title,
            "value": property.value,
            "type": property.type,
            "owner_id": property.owner_id,
            "address": property.address,
            "status": property.status,
            "area": property.area,
            "rooms": property.rooms,
            "bathrooms": property.bathrooms
        })

    return {"properties": result}

class PropertyViewSchema(BaseModel):
    """ Define como um imóvel será retornado: imóvel + comentários.
    """
    title: str = "Casa dos Sonhos"
    value: float = 500000.00
    type: str = "house"
    owner_id: int = 1
    address: str = "Rua dos Sonhos, 123"
    status: str = "available"
    area: int = 200
    rooms: int = 4
    bathrooms: int = 3

class PropertyDeleteSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    title: str

def show_property(property: PropertySchema):
    """ Retorna uma representação do imóvel seguindo o schema definido em
        PropertyViewSchema.
    """
    return {
        "title": property.title,
        "value": property.value,
        "type": property.type,
        "owner_id": property.owner_id,
        "address": property.address,
        "status": property.status,
        "area": property.area,
        "rooms": property.rooms,
        "bathrooms": property.bathrooms
    }