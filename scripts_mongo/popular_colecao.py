from pymongo import MongoClient
from datetime import datetime
from variables import *  # Importe suas variáveis de conexão (uri, etc.)

# Create a new client and connect to the server
client = MongoClient(uri)

# Conectando ao seu cluster do MongoDB
database = client["DatabaseData"]
colecao = database["tableData"]

# Lista de documentos
documentos = [
  {
    "nome_suite": "Login",
    "id_suite": 1,
    "tempo_inicio_teste": "2023-12-16T08:00:00Z",
    "tempo_fim_teste": "2023-12-16T08:15:00Z",
    "tempo_total_teste": 15,
    "resultado_teste": "passou",
    "num_testes_executados": 20
  },
  {
    "nome_suite": "Carrinho",
    "id_suite": 2,
    "tempo_inicio_teste": "2023-12-16T09:30:00Z",
    "tempo_fim_teste": "2023-12-16T09:45:00Z",
    "tempo_total_teste": 15,
    "resultado_teste": "passou",
    "num_testes_executados": 15
  },
  {
    "nome_suite": "Pagamento",
    "id_suite": 3,
    "tempo_inicio_teste": "2023-12-16T10:20:00Z",
    "tempo_fim_teste": "2023-12-16T11:00:00Z",
    "tempo_total_teste": 40,
    "resultado_teste": "falhou",
    "num_testes_executados": 35
  },
  {
    "nome_suite": "Cadastro",
    "id_suite": 4,
    "tempo_inicio_teste": "2023-12-16T11:30:00Z",
    "tempo_fim_teste": "2023-12-16T11:45:00Z",
    "tempo_total_teste": 15,
    "resultado_teste": "passou",
    "num_testes_executados": 25
  },
  {
    "nome_suite": "Pesquisa",
    "id_suite": 5,
    "tempo_inicio_teste": "2023-12-16T13:00:00Z",
    "tempo_fim_teste": "2023-12-16T13:25:00Z",
    "tempo_total_teste": 25,
    "resultado_teste": "passou",
    "num_testes_executados": 30
  },
  {
    "nome_suite": "Configurações",
    "id_suite": 6,
    "tempo_inicio_teste": "2023-12-16T14:00:00Z",
    "tempo_fim_teste": "2023-12-16T14:45:00Z",
    "tempo_total_teste": 45,
    "resultado_teste": "falhou",
    "num_testes_executados": 40
  },
  {
    "nome_suite": "Dashboard",
    "id_suite": 7,
    "tempo_inicio_teste": "2023-12-16T15:30:00Z",
    "tempo_fim_teste": "2023-12-16T15:45:00Z",
    "tempo_total_teste": 15,
    "resultado_teste": "passou",
    "num_testes_executados": 18
  },
  {
    "nome_suite": "Notificações",
    "id_suite": 8,
    "tempo_inicio_teste": "2023-12-16T16:00:00Z",
    "tempo_fim_teste": "2023-12-16T16:30:00Z",
    "tempo_total_teste": 30,
    "resultado_teste": "falhou",
    "num_testes_executados": 22
  },
  {
    "nome_suite": "Perfil",
    "id_suite": 9,
    "tempo_inicio_teste": "2023-12-16T17:00:00Z",
    "tempo_fim_teste": "2023-12-16T17:20:00Z",
    "tempo_total_teste": 20,
    "resultado_teste": "passou",
    "num_testes_executados": 27
  },
  {
    "nome_suite": "Estatísticas",
    "id_suite": 10,
    "tempo_inicio_teste": "2023-12-16T18:00:00Z",
    "tempo_fim_teste": "2023-12-16T18:30:00Z",
    "tempo_total_teste": 30,
    "resultado_teste": "passou",
    "num_testes_executados": 35
  }
]


# Convertendo strings para objetos de datetime e removendo o campo _id
for doc in documentos:
    doc['tempo_inicio_teste'] = datetime.strptime(doc['tempo_inicio_teste'], '%Y-%m-%dT%H:%M:%SZ')
    doc['tempo_fim_teste'] = datetime.strptime(doc['tempo_fim_teste'], '%Y-%m-%dT%H:%M:%SZ')
    doc.pop('_id', None)  # Removendo o campo _id se existir

# Inserindo os documentos na coleção
colecao.insert_many(documentos)

print("Documentos inseridos com sucesso!")



