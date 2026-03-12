import enum

from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class PropertyType(enum.Enum):
    HOUSE = "house"
    APARTMENT = "apartment"
    COMERCIAL = "commercial"
    LAND = "land"


class Property(Base):
    __tablename__ = 'property'

    id = Column("pk_property", Integer, primary_key=True)
    name = Column(String(140), unique=True)
    description = Column(String(280))
    rent_value = Column(Float)
    due_date = Column(DateTime, default=datetime.now())
    type = Column(enum.Enum(PropertyType), nullable=False)

    owner_id = Column(Integer, ForeignKey("owner.pk_owner"))
    owner = relationship("Owner", back_populates="property")

    creation_date = Column(DateTime, default=datetime.now())
    last_update = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, name:str, description:str, rent_value:float, due_date:Union[DateTime, None] = None, 
                 type:PropertyType):
        """
        Cria um Imóvel

        Arguments:
            name: nome do produto.
            description: descrição do produto.
            rent_value: valor do aluguel.
            due_date: data de vencimento.
            type: tipo do imóvel.
            owner: proprietário do imóvel.
        """
        self.name = name
        self.description = description
        self.rent_value = rent_value
        self.due_date = due_date
        self.type = type.value
        self.owner_id = self.owner_id
        self.creation_date = datetime.now()
        self.last_update = datetime.now()