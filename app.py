from datetime import datetime
from flask_openapi3 import OpenAPI, Info, Tag # type: ignore
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Float

from model import Session, Property, Owner
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API de Imóveis", version="1.0.0", description="API para gerenciamento de imóveis")
app = OpenAPI(__name__, info=info)
CORS(app)

# @app.route("/")
# def home():
#     return "Hello, Flask!"

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
property_tag = Tag(name="Propriedade", description="Adição, visualização e remoção de propriedades à base")
owner_tag = Tag(name="Proprietário", description="Adição, visualização e remoção de proprietários à base")

@app.post('/property', tags=[property_tag], responses={"200": PropertyViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_property(form: PropertySchema):
    """Adiciona um novo Imóvel à base de dados

    Retorna uma representação dos imóveis associados.
    """
    # converted_due_date = datetime.fromisoformat(form.due_date.replace('Z', '+00:00'))
    property = Property(
        title=form.title,
        value=form.value,
        type=form.type,
        owner_id=form.owner_id,
        address=form.address,
        status=form.status,
        area=form.area,
        rooms=form.rooms,
        bathrooms=form.bathrooms)
    try:
        # criando conexão com a base
        session = Session()
        # adicionando imóvel
        session.add(property)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado imóvel de nome: '{property.title}'")
        return show_property(property), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Imóvel de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar imóvel '{property.title}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar imóvel '{property.title}', {error_msg}")
        return {"message": error_msg}, 400

@app.get('/property', tags=[property_tag], responses={"200": ListPropertiesSchema, "400": ErrorSchema})
def get_properties():
    """Faz a busca por todos os imóveis cadastrados na base de dados

    Retorna uma representação dos imóveis associados.
    """
    try:
        # criando conexão com a base
        session = Session()
        # buscando todos os imóveis
        properties = session.query(Property).all()
        logger.debug(f"{len(properties)} imóveis encontrados")
        return show_properties(properties), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível buscar os itens :/"
        logger.warning(f"Erro ao buscar imóveis, {error_msg}")
        return {"message": error_msg}, 400

@app.post('/owner', tags=[owner_tag], responses={"200": OwnerViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_owner(form: OwnerSchema):
    """Adiciona um novo Proprietário à base de dados

    Retorna uma representação dos proprietários associados.
    """
    owner = Owner(
        name=form.name,
        email=form.email,
        phone=form.phone)
    try:
        # criando conexão com a base
        session = Session()
        # adicionando proprietário
        session.add(owner)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado proprietário de nome: '{owner.name}'")
        return show_owner(owner), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = str(e)
        logger.warning(f"Erro ao adicionar proprietário '{owner.name}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar proprietário '{owner.name}', {error_msg}")
        return {"message": error_msg}, 400
    
@app.get('/owner', tags=[owner_tag], responses={"200": ListOwnersSchema, "400": ErrorSchema})
def get_owners():
    """Faz a busca por todos os proprietários cadastrados na base de dados

    Retorna uma representação dos proprietários associados.
    """
    try:
        # criando conexão com a base
        session = Session()
        # buscando todos os proprietários
        owners = session.query(Owner).all()
        logger.debug(f"{len(owners)} proprietários encontrados")
        return show_owners(owners), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível buscar os itens :/"
        logger.warning(f"Erro ao buscar proprietários, {error_msg}")
        return {"message": error_msg}, 400