from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from schemas import EventoCreateSchema, EventoUpdateSchema, EventoViewSchema, EventoDeleteSchema, ErrorSchema
import requests

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

evento_tag = Tag(name='Evento', description='Cadastro, consulta, edição e deleção de um evento')

def get_weather(cidade):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&units=metric&APPID=c77725ea319dd9abff5e398efb74aa1c"
        response = requests.get(url)
        data = response.json()
        temperatura = round(data["main"]["temp"])
        return f"{temperatura}ºC"
    except Exception as e:
        return str(e)

@app.get('/eventos', tags=[evento_tag], responses={"200": EventoViewSchema})
def get_eventos():
    response = requests.get('http://database_service:5001/eventos')
    eventos = response.json()

    for evento in eventos:
        cidade = evento.get('cidade')
        if cidade:
            temperatura = get_weather(cidade)
            evento['temperatura'] = temperatura

    return jsonify(eventos), response.status_code

@app.post('/eventos', tags=[evento_tag], responses={"200": EventoCreateSchema, "409": ErrorSchema, "400": ErrorSchema})
def criar_evento(form: EventoCreateSchema):
    data = form.dict()
    response = requests.post('http://database_service:5001/eventos', json=data)
    evento_data = response.json()
    temperatura = get_weather(evento_data['cidade'])
    evento_data['temperatura'] = temperatura
    return jsonify(evento_data), response.status_code

@app.put('/eventos', tags=[evento_tag], responses={"200": EventoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def atualizar_evento(form: EventoUpdateSchema):
    data = form.dict()
    response = requests.put(f'http://database_service:5001/eventos/{data["id"]}', json=data)
    evento_data = response.json()
    temperatura = get_weather(evento_data['cidade'])
    evento_data['temperatura'] = temperatura
    return jsonify(evento_data), response.status_code

@app.delete('/eventos', tags=[evento_tag], responses={"200": {"message": "Evento removido com sucesso"}, "404": ErrorSchema})
def deletar_evento(form: EventoDeleteSchema):
    data = form.dict()
    response = requests.delete(f'http://database_service:5001/eventos/{data["id"]}')
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
