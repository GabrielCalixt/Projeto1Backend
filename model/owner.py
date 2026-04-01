from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from model import Base

class Owner(Base):
    __tablename__ = 'owner'

    id = Column("pk_owner", Integer, primary_key=True)
    name = Column(String(140), unique=True)
    email = Column(String(280), unique=True)
    phone = Column(String(20))
    properties = relationship(
        "Property",
        back_populates="owner",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )

    def __init__(self, name:str, email:str, phone:str | int):
        """
        Cria um Proprietário

        Arguments:
            name: nome do proprietário.
            email: email do proprietário.
            phone: telefone do proprietário.
        """
        self.name = name
        self.email = email
        self.phone = phone
