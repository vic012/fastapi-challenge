from pydantic import BaseModel
from typing import Union


# Usado para definir (Validar) os dados com relação aos seus tipos no schema
class VideoBase(BaseModel):
	title: str
	description: str
	url: str

	class Config:
		orm_mode = True

# Usado para visualizar os dados
class Video(BaseModel):
	id: int
	title: str
	description: str
	url: str

	# O Pydantic orm_modedirá ao modelo Pydantic para ler os dados, mesmo que não seja um dict,
	# mas um modelo ORM (ou qualquer outro objeto arbitrário com atributos).
	# Dessa forma, em vez de apenas tentar obter o idvalor de a dict, como em:
	# id = data["id"]
	# ele também tentará obtê-lo de um atributo, como em:
	# id = data.id
	class Config:
		orm_mode = True
