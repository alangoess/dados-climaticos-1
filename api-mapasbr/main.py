from fastapi import FastAPI
from requests import *
from fastapi.middleware.cors import CORSMiddleware
import main

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/{lat}/{long}")
async def root(lat: str,long: str):
    chave_api = '70c85c4d9e45c8a96fd7ab5d1efaec5e' # permite a comunicação da API com a aplicação 
    
    try: 
        link = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={chave_api}&lang=pt_br'

        requisicao = get(link).json() # O metdo get serve para captar o link da API e o metodo JSON serve para converter os dados informados pela API em listas e dicionarios python 
        nomeCidade = requisicao['name']
        descricao = requisicao['weather'][0]['description'] # ['weather'][0] é o campo onde a descrição está dentro o campo ['description'] serve apenas para pegar a informação de descrição do céu/temperatura que está dentro de ['weather'][0] 
        temperatura = requisicao['main']['temp']- 273.15 #
    
        return {"message": f'Sua cidade é {nomeCidade}, O tempo agora está {descricao}, a temperatura é',
        "temperatura":f'{temperatura:.0f}°C'       
                }
    except Exception as e:
        return {"message": f'Não foi possivel encontrar Latitude {lat} e Longitude {long}' }
  