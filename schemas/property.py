from pydantic import BaseModel
from typing import Optional, List
from model.owner import Owner

class PropertySchema(BaseModel):
    """ Define como uma nova propriedade a ser inserida deve ser representada
    """
    name: str = "Casa dos Sonhos"
    description: str = "Uma casa maravilhosa com vista para o mar."
    rent_value: float = 2500.00
    due_date: Optional[str] = None
    type: str = "house"
    owner_id: int = 1


class PropertySearchSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da propriedade.
    """
    name: str = "Casa dos Sonhos"


class ListPropertiesSchema(BaseModel):
    """ Define como uma listagem de propriedades será retornada.
    """
    properties: List[PropertySchema]


def show_properties(properties: List[PropertySchema]):
    """ Retorna uma representação da propriedade seguindo o schema definido em
        PropertyViewSchema.
    """
    result = []
    for property in properties:
        result.append({
            "name": property.name,
            "description": property.description,
            "rent_value": property.rent_value,
            "due_date": property.due_date,
            "type": property.type,
            "owner_id": property.owner_id
        })

    return {"properties": result}


class PropertyViewSchema(BaseModel):
    """ Define como um imóvel será retornado: imóvel + comentários.
    """
    id: int = 1
    name: str = "John Doe"
    email: str = "john.doe@example.com"
    phone: str = "1234567890"


class PropertyDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    name: str

def show_property(property: PropertySchema):
    """ Retorna uma representação do imóvel seguindo o schema definido em
        PropertyViewSchema.
    """
    return {
        "name": property.name,
        "description": property.description,
        "rent_value": property.rent_value,
        "due_date": property.due_date,
        "type": property.type,
        "owner_id": property.owner_id
    }