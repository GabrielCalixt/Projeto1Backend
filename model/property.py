import enum

from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Property(Base):
    __tablename__ = 'property'

    id = Column("pk_property", Integer, primary_key=True)
    title = Column(String(140), unique=True)
    value = Column(Float, nullable=False)
    # due_date = Column(DateTime, default=datetime.now(), nullable=True)
    type = Column(String(140), nullable=False)
    address = Column(String(140), nullable=False)
    status = Column(String(140), nullable=False)
    area = Column(Integer, nullable=False)
    rooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)

    owner_id = Column(Integer, ForeignKey("owner.pk_owner"))
    owner = relationship("Owner", back_populates="properties")

    creation_date = Column(DateTime, default=datetime.now())
    last_update = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, title:str, value:float, type:str, owner_id:int, address:str, status:str, area:int, rooms:int, bathrooms:int):
        """
        Cria um Imóvel

        Arguments:
            title: título do imóvel.
            value: valor do imóvel.
            type: tipo do imóvel.
            owner_id: ID do proprietário do imóvel.
            address: endereço do imóvel.
            status: status do imóvel.
            area: área do imóvel.
            rooms: número de quartos do imóvel.
            bathrooms: número de banheiros do imóvel.
        """
        self.title = title
        self.value = value
        self.type = type
        self.owner_id = owner_id
        self.address = address
        self.status = status
        self.area = area
        self.rooms = rooms
        self.bathrooms = bathrooms
        # self.creation_date = datetime.now()
        # self.last_update = datetime.now()