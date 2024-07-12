from pydantic import BaseModel, validator
from datetime import datetime, date

# Schema para criar um novo evento
class EventoCreateSchema(BaseModel):
    nome: str = 'Rock in rio'
    cidade: str = 'Rio de Janeiro'
    data_evento: str = '2024-11-11'

    @validator('data_evento')
    def check_date_format(cls, value):
        try:
            parsed_date = datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("O formato da data deve ser YYYY-MM-DD")
        if parsed_date <= date.today():
            raise ValueError("A data do evento deve ser uma data futura")
        return value

# Schema para atualizar um evento existente
class EventoUpdateSchema(BaseModel):
    id: int = 1
    nome: str = 'Isso não é uma festa'
    cidade: str = 'São paulo'
    data_evento: str = '2024-12-12'

    @validator('data_evento')
    def check_date_format(cls, value):
        try:
            parsed_date = datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("O formato da data deve ser YYYY-MM-DD")
        if parsed_date <= date.today():
            raise ValueError("A data do evento deve ser uma data futura")
        return value

# Schema para visualizar um evento
class EventoViewSchema(BaseModel):
    id: int
    nome: str
    cidade: str
    data_evento: str

# Schema para deletar um evento
class EventoDeleteSchema(BaseModel):
    id: int = 1

# Schema para mensagens de erro
class ErrorSchema(BaseModel):
    message: str
