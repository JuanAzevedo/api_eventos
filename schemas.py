from pydantic import BaseModel, validator
from datetime import datetime, date

# Schema para criar um novo evento
class EventoCreateSchema(BaseModel):
    nome: str
    cidade: str
    data_evento: str

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
    id: int
    nome: str
    cidade: str
    data_evento: str

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
    id: int

# Schema para mensagens de erro
class ErrorSchema(BaseModel):
    message: str
